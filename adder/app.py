from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True)  
    

@app.route("/compute", methods=["GET"])
def compute():
    
    nums = r.lrange('sum_list', 0, -1)
    if not nums:
        return jsonify({"error": "No data in 'sum_list' list!"}), 400
    
    try:
        nums_int = [int(x) for x in nums]
    except ValueError:
        return jsonify({"error": "Non-integer value in Redis list!"}), 400
    
    result = sum(nums_int)
    r.lpush('sum_result', result)
    
    return jsonify({"service": "adder", "input": nums_int, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
