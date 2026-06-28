class FutureLetterEngine:
    def write(self, recipient, year, message):
        return {'to': recipient, 'open_in': year, 'message': message}
