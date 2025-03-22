import streamlit as st

st.title('Welcome to H1 Second Floor Stand App')
st.write('This is to prevent any conflicts and not to piss me (Noel) off')

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

def exitstand():
    stand1 = open('stand1.txt', 'r').read().splitlines()
    stand2 = open('stand2.txt', 'r').read().splitlines()
    
    if name in stand1:
        stand1.remove(name)
        with open('stand1.txt', 'w') as f:
            f.write('\n'.join(stand1))
    elif name in stand2:
        stand2.remove(name)
        with open('stand2.txt', 'w') as f:
            f.write('\n'.join(stand2))

def enter_queue():
    stand1_list = open('stand1.txt', 'r').read().splitlines()
    stand2_list = open('stand2.txt', 'r').read().splitlines()
    
    if len(stand1_list) <= len(stand2_list):
        stand1_list.append(name)
        open('stand1.txt', 'w').write('\n'.join(stand1_list))

    else:
        stand2_list.append(name)
        open('stand2.txt', 'w').write('\n'.join(stand2_list))

def veto():
    if name not in ['Noel', 'Mehul']:
        st.write('Get the hell out!')
        return
    
    with st.form(key='veto_form'):
        if name == 'Noel':
            answer = st.text_input('What is your Dubai license plate number?')
        else:
            answer = st.text_input('What is your favorite COC troop?')

        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if name == 'Noel' and answer == 'H68019':
                st.write('Veto successful')
            elif name != 'Noel' and answer == 'bad food':
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
            else:
                stand2 = [name] + stand2
                with open('stand2.txt', 'w') as f:
                    f.write('\n'.join(stand2))
    
name = st.text_input('Enter your name')

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
    st.button('Enter Queue', on_click=enter_queue)
with col2:
    st.button('Veto', on_click=veto)
with col3:
    st.button('View Stand 1', on_click=view_stand1)
with col4:
    st.button('View Stand 2', on_click=view_stand2)
with col5:
    st.button('Exit', on_click=exitstand)