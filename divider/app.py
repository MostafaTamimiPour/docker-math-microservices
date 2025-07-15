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

    nums1 = r.lrange('sum_list', 0, -1)
    nums2 = r.lrange('sub_list', 0, -1)
    if not nums1 or not nums2:
        return jsonify({"error": "Empty list in 'sum_list' or 'sub_list'!"}), 400

    try:
        nums1_int = [int(x) for x in nums1]
        nums2_int = [int(x) for x in nums2]
    except ValueError:
        return jsonify({"error": "Non-integer value in Redis lists!"}), 400

    sum1 = sum(nums1_int)
    sum2 = sum(nums2_int)

    if sum2 == 0:
        return jsonify({"error": "Division by zero!"}), 400

    result = sum1 / sum2  

    r.lpush('div_result', result)
    
    
    return jsonify({"service": "divider", "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
