import ast
import difflib
import os
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Class for detecting code smells
class CodeSmellDetector:
    def __init__(self, code, long_method_threshold=12, god_class_method_threshold=5, large_param_threshold=5):
        self.code = code
        self.long_method_threshold = long_method_threshold
        self.god_class_method_threshold = god_class_method_threshold
        self.large_param_threshold = large_param_threshold
        self.smells = []

    def detect_long_method(self, node):
        if isinstance(node, ast.FunctionDef):
            method_length = len(node.body)
            if method_length > self.long_method_threshold:
                self.smells.append(f"Long Method detected: {node.name}, Lines: {method_length}")

    def detect_large_parameter_list(self, node):
        if isinstance(node, ast.FunctionDef):
            num_params = len(node.args.args)
            if num_params > self.large_param_threshold:
                self.smells.append(f"Large Parameter List detected: {node.name}, Parameters: {num_params}")

    def detect_god_class(self, class_node):
        method_count = sum(1 for node in class_node.body if isinstance(node, ast.FunctionDef))
        class_length = len(class_node.body)
        if method_count > self.god_class_method_threshold or class_length > 200:
            self.smells.append(f"God Class detected: {class_node.name}, Methods: {method_count}, Lines: {class_length}")

    def detect_code_smells(self):
        tree = ast.parse(self.code)

        for node in ast.walk(tree):
            # Long Method detection
            self.detect_long_method(node)

            # Large Parameter List detection
            self.detect_large_parameter_list(node)

            # God Class detection
            if isinstance(node, ast.ClassDef):
                self.detect_god_class(node)

    def detect_duplicated_code(self):
        lines = self.code.splitlines()

        for i, line1 in enumerate(lines):
            for j, line2 in enumerate(lines[i + 1:], start=i + 1):
                if line1.strip() and difflib.SequenceMatcher(None, line1, line2).ratio() > 0.9:
                    self.smells.append(f"Duplicated code detected between line {i + 1} and line {j + 1}")

    def get_smells(self):
        self.detect_code_smells()
        self.detect_duplicated_code()
        return self.smells

@app.route("/detect-smells", methods=["POST"])
def detect_smells():
    # Extract code from the request body
    code = request.form.get("code")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Create a CodeSmellDetector instance and detect smells
    detector = CodeSmellDetector(code)
    smells = detector.get_smells()

    # Return the detected smells as JSON
    return jsonify({"smells": smells})

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

