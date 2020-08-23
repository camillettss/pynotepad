import PySimpleGUI as psg
import pathlib

psg.ChangeLookAndFeel('Dark')

winw=90
winh=25
file=None

menu_layout=[['File', ['New (Ctrl+N)', 'Save (Ctrl+S)', ' --- ', 'Exit']],
            ['Tools', ['Open (Ctrl+O)']],
            ['Help', ['About', 'How To']]]

layout= [[psg.Menu(menu_layout)],
        [psg.Text('New File', font=('Consolas', 10), size=(winw, 1), key='_INFO_')],
        [psg.Multiline(font=('Consolas', 10), size=(winw, winh), key='_BODY_')]]

win = psg.Window('camillettss notepad', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
win.maximize()
win['_BODY_'].expand(expand_x=True, expand_y=True)

def new_file():
    win['_BODY_'].update(value='')
    win['_INFO_'].update(value='New File')
    file=None
    return file

def save_file(file):
    '''Save file instantly if already open; otherwise use `save-as` popup'''
    if file:
        file.write_text(values.get('_BODY_'))
        psg.popup_no_buttons('Saved', auto_close=True, auto_close_duration=0.6)
    else:
        save_file_as()

def save_file_as():
    '''Save new file or save existing file with another name'''
    filename = psg.popup_get_file('Save As', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        win['_INFO_'].update(value=file.absolute())
        return file

def open_file():
    filename=psg.popup_get_file('Open', no_window=True)
    if filename:
        file=pathlib.Path(filename)
        win['_BODY_'].update(value=file.read_text())
        win['_INFO_'].update(value=file.absolute())
        return file

def how_to():
    text='check my instagram profile, @_camillettss_ for tutorials!'
    psg.popup_auto_close(text, title='how to', auto_close=False)

def about_me():
    '''A short, pithy quote'''
    psg.popup_no_wait("hi, i am Francesco Camilletti, @_camillettss_ on instagram, i am a python developer that wishes u'll like this notepad :)")

while True:
    event, values = win.read()
    if event in('Exit', None):
        break
    if event in ('New (Ctrl+N)', 'n:78'):
        file = new_file()
    if event in ('Save (Ctrl+S)', 's:83'):
        save_file(file)
    if event in ('Open (Ctrl+O)', 'o:79'):
        open_file()
    if event in ('About',):
        about_me()
    if event in ('How To',):
        how_to()