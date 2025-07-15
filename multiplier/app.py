from flask import Flask, jsonify
import math
import os
import redis

app = Flask(__name__)

@app.route("/compute", methods=["GET"])
def compute():
    result = math.prod(range(1, 11))  # 1*2*...*10
    r = redis.Redis(
        host=os.getenv('REDIS_HOST', 'redis'),
        port=int(os.getenv('REDIS_PORT', 6379))
    )
    r.lpush('result_multiply', result)
    
    
    return jsonify({"service": "multiplier", "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
