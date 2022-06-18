#Dekorator

class QuoteText:
    
    def __init__(self, text):
        self._text = text
  
    def render(self):
        return self._text

class QuotationMarks(QuoteText):
  
    def __init__(self, wrapped):
        self._wrapped = wrapped
  
    def render(self):
        return '"{}"'.format(self._wrapped.render())
    
class Italics(QuoteText):
  
    def __init__(self, wrapped):
        self._wrapped = wrapped
  
    def render(self):
        return '<i> {} <i>'.format(self._wrapped.render())

    
text = QuoteText("Marzenie jest formą planowania")
Quote = Italics(QuotationMarks(text))
  
print("Cytat bez formatowania:", text.render())
print("Cytat z formatowaniem :", Quote.render())