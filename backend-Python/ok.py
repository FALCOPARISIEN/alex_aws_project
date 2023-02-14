from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
    {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
    {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
]

@app.route('/api/v1/employees', methods=['GET'])
def get_all_employees():
    return jsonify(employees)

@app.route('/api/v1/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    employee = next((emp for emp in employees if emp['id'] == id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)