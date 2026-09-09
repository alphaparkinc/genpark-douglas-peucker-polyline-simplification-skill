"""MCP Server for Douglas-Peucker Simplification Skill."""
import json
import sys
from client import DouglasPeucker

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "simplify_trajectory",
                            "description": "Simplify polyline trajectory via Douglas-Peucker algorithm",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "points": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    },
                                    "epsilon": {"type": "number"}
                                },
                                "required": ["points", "epsilon"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                pts = [tuple(p) for p in args["points"]]
                eps = float(args["epsilon"])
                out_pts = DouglasPeucker.simplify(pts, eps)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{
                            "type": "text",
                            "text": json.dumps({
                                "simplified_points": out_pts,
                                "original_count": len(pts),
                                "simplified_count": len(out_pts),
                                "compression_ratio": round(len(out_pts) / len(pts), 4)
                            })
                        }]
                    }
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
