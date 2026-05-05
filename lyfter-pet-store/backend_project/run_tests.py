import pytest

# executes all tests inside the 'tests' folder
exit_code = pytest.main(["app/tests", "-q", "--tb=short"])

# exit_code = 0 -> all passed
# exit_code = 1 -> some failed
if exit_code == 0:
    print("\n✅ All tests passed correctly.")
else:
    print(f"\n❌ Some tests failed, exit code: {exit_code}")
