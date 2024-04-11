from django.http import JsonResponse
from robot.api import TestSuiteBuilder
import os
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def execute_tests(request):
    # Handle only POST requests
    if request.method == 'POST':
        try:
            # Parse JSON payload
            test_data = json.loads(request.body)

            # Get the current package directory
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Create the Robot test file dynamically in the current package directory
            test_file_path = os.path.join(current_dir, 'test.robot')
            with open(test_file_path, 'w') as f:
                # Write Robot Framework settings
                # defaultly added this for automation purpose
                f.write("*** Settings ***\n")
                f.write("Library    SeleniumLibrary\n\n")
                f.write("*** Test Cases ***\n") 

                # Check if any tests are provided
                if len(test_data['tests']) == 0:
                    raise Exception("No Tests found in the JSON Request")

                # Write test cases and steps to the test file
                for test in test_data['tests']:
                    f.write(test['title'] + "\n")

                    # Check if any steps are provided for the test
                    if len(test['steps']) == 0:
                        raise Exception("No steps found in the test")

                    # Write each step with correct formatting
                    for step in test['steps']:
                        # Replace single quotes with double quotes
                        step = step.replace("'", '')
                        f.write("    " + step + "\n")

            # Execute the Robot test file
            suite = TestSuiteBuilder().build(test_file_path)
            result = suite.run()

            # Format test results for API response
            test_results = {
                'total_tests': result.statistics.total.total,
                'total_passed': result.statistics.total.passed,
                'total_failed': result.statistics.total.failed,
                # Return True if all tests passed, False otherwise
                'output': result.return_code == 0  
            }

            # Convert test_results to JSON and return as a JSON response
            return JsonResponse(test_results)

        except Exception as e:
            # Handle exceptions while wrtie to file or looping throw the Json Response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return error for unsupported HTTP methods(Other than POST Request)
        return JsonResponse({'error': 'Method not allowed'}, status=405)
