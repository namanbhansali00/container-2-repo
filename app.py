# from flask import Flask, request, jsonify
# import os

# app = Flask(__name__)

# PERSISTENT_VOLUME_PATH = "/Naman_PV_dir"

# @app.route('/calculate', methods=['POST'])
# def calculate():
#     data = request.json
#     if not data or 'file' not in data or 'product' not in data:
#         return jsonify({"file": None, "error": "Invalid JSON input."}), 400

#     file_name = data['file']
#     product = data['product']

#     try:
#         with open(os.path.join(PERSISTENT_VOLUME_PATH, file_name), 'r') as f:
#             lines = f.readlines()
#         total = sum(int(line.split(',')[1]) for line in lines[1:] if line.split(',')[0] == product)
#         return jsonify({"file": file_name, "sum": total})
#     except FileNotFoundError:
#         return jsonify({"file": file_name, "error": "File not found."}), 404
#     except Exception as e:
#         return jsonify({"file": file_name, "error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8081)
import csv

# Reused my Assignment-1 code here.

from flask import Flask, request

app = Flask(__name__)

@app.route("/sum", methods=["POST"])
def sum():
    sum = 0

    # Reference: https://docs.python.org/3/library/csv.html
    # I have used the basic quick-start code given in the docs of python csv parsing library. (From Section "A short usage example:")
    # I have modified the loop with my own logic to do the sum and for throwing error for invalid CSV.

    # 1. Calculate sum of the product amounts
    with open("/Naman_PV_dir/"+request.json["file"]) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if len(row) != 2:
                return { 
                        "file": request.json["file"], 
                        "error": "Input file not in CSV format." 
                       }
            if(row[0] == request.json["product"]):
                sum = sum + int(row[1])

    # 2. return the sum along with the file name.
    return { 
            "file": request.json["file"], 
            "sum": sum
        }

if __name__ == "__main__":
    app.json.sort_keys = False
    app.run(host="0.0.0.0", port=8081)
