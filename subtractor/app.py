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


    nums = r.lrange('sub_list', 0, -1)
    if not nums:
        return jsonify({"error": "No data in 'numbers' list!"}), 400
    
    try:
        nums_int = [int(x) for x in nums]
    except ValueError:
        return jsonify({"error": "Non-integer value in Redis list!"}), 400
    
    total = sum(nums_int)
    
    result = 1000 - total            
    r.lpush('sub_result', result)
 
    return jsonify({"service": "subtractor", "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
