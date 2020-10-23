from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
class author(Form):
  _name = TextField('')
  _gmail = TextField('')
  _subject = TextField('requests from user')
  _message = TextAreaField('')
  _send = SubmitField('aquacodetermux@gmail.com')
  
