def multiply(num1, num2):
    return int(num1) * int(num2)


def print_text(text, request):
    response = request.get('some_url')
    return response.text


def test_multiply(self):
      result = multiply(1, 2)
      self.assertEqual(result, 2)
      
      result = multiply(-999999999999999, 0)
      self.assertEqual(result, 0)

      result = multiply(-999999999999999, 1)
      self.assertEqual(result, -999999999999999)

      result = multiply(-1, -1)
      self.assertEqual(result, 1)



class Response:
    def __init__(self):
        self.text = 'Test passed!'

class Requests:
    def __init__(self):
        pass

    def get(self, url):
        return Response()

