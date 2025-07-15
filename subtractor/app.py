from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

@app.route("/compute", methods=["GET"])
def compute():
    total = sum(range(1, 11))    # 1+2+...+10 = 55
    result = 100 - total         # 100 - 55 = 45

    r = redis.Redis(
        host=os.getenv('REDIS_HOST', 'redis'),
        port=int(os.getenv('REDIS_PORT', 6379))
    )
    r.lpush('result_subtract', result)
 
    return jsonify({"service": "subtractor", "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
