import streamlit as st

stand_users = open('names.txt', 'r').read().splitlines()

st.title('Welcome to H1 Second Floor Stand App')
st.write('This is to prevent any conflicts and not to piss me (Noel) off')

noels_answer = st.secrets["noels_answer"]
mehuls_answer = st.secrets["mehuls_answer"]


def view_stand1():
    st.write('Stand 1:')
    stand1 = open('stand1.txt', 'r').read().splitlines()
    for i, name in enumerate(stand1):
        st.write(f'{i+1}. {name}')

def view_stand2():
    st.write('Stand 2:')
    stand2 = open('stand2.txt', 'r').read().splitlines()
    for i, name in enumerate(stand2):
        st.write(f'{i+1}. {name}')

def exitstand(name):
    stand1 = open('stand1.txt', 'r').read().splitlines()
    stand2 = open('stand2.txt', 'r').read().splitlines()
    name = name.title()
    if name in stand1:
        stand1.remove(name)
        with open('stand1.txt', 'w') as f:
            f.write('\n'.join(stand1))
    elif name in stand2:
        stand2.remove(name)
        with open('stand2.txt', 'w') as f:
            f.write('\n'.join(stand2))

def enter_queue(name):
    name = name.title()
    stand1_list = open('stand1.txt', 'r').read().splitlines()
    stand2_list = open('stand2.txt', 'r').read().splitlines()

    if name in stand1_list or name in stand2_list:
        st.write('You are already in the queue. Buzz off!')
        return
    
    if len(stand1_list) <= len(stand2_list):
        stand1_list.append(name)
        open('stand1.txt', 'w').write('\n'.join(stand1_list))
        st.write('You have been added to Stand 1 after ' + stand1_list[-2])

    else:
        stand2_list.append(name)
        open('stand2.txt', 'w').write('\n'.join(stand2_list))
        st.write('You have been added to Stand 2 after ' + stand2_list[-2])

def veto(name):
    name = name.title()
    if name not in ['Noel', 'Mehul']:
        st.write('Get the hell out!')
        return
    
    with st.form(key='veto_form'):
        if name == 'Noel':
            answer = st.text_input("What is your mom's family name?")
        else:
            answer = st.text_input('What is your your favourite meccademia prof?')

        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if name == 'Noel' and answer.lower() == noels_answer:
                st.write('Veto successful')
            elif name != 'Noel' and answer.lower() == mehuls_answer:
                st.write('Veto successful')
            else:
                st.write('Veto failed')
                return

            stand1 = open('stand1.txt', 'r').read().splitlines()
            stand2 = open('stand2.txt', 'r').read().splitlines()
            if len(stand1) <= len(stand2):
                stand1 = [name] + stand1
                with open('stand1.txt', 'w') as f:
                    f.write('\n'.join(stand1))

                st.write('You have been added to Stand 1')
            else:
                stand2 = [name] + stand2
                with open('stand2.txt', 'w') as f:
                    f.write('\n'.join(stand2))
                
                st.write('You have been added to Stand 2')
    
name = st.text_input('Enter your name')

if name.title() not in stand_users:
    st.write('You are not allowed to use this app')
    st.stop()

button_style = """
    <style>
        div.stButton > button {
            width: 100%;
            height: 50px;
            font-size: 16px;
        }
    </style>
"""

st.markdown(button_style, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button('Enter Queue', on_click=lambda: enter_queue(name))
with col2:
    st.button('Veto', on_click=lambda: veto(name))
with col3:
    st.button('View Stand 1', on_click=view_stand1)
with col4:
    st.button('View Stand 2', on_click=view_stand2)
with col5:
    st.button('Exit', on_click=lambda: exitstand(name))