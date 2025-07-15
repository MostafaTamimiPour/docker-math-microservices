from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

@app.route("/compute", methods=["GET"])
def compute():

    results =  100 / 10
    r = redis.Redis(
        host=os.getenv('REDIS_HOST', 'redis'),
        port=int(os.getenv('REDIS_PORT', 6379))
    )
    r.lpush('result_divide', results)
    
    
    return jsonify({"service": "divider", "result": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
