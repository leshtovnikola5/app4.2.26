import streamlit as st

st.write(" Тест - История ")

st.write("През коя година започва Първата световна война?")
q1 = st.text_input("Отговор:", key="q1")

st.write("Коя държава излиза победител след Първата световна война?")
q2 = st.text_input("Отговор:", key="q2")

st.write("Коя страна напада Полша през 1939 г.?")
q3 = st.text_input("Отговор:", key="q3")

st.write("Кой е лидер на болшевиките?")
q4 = st.text_input("Отговор:", key="q4")

st.write("Кога започва Втората световна война?")
q5 = st.text_input("Отговор:", key="q5")

if st.button("Проверка"):
    tochki = 1

    if q1 == "1914":
        tochki += 1

    if q2 == "Антантата":
        tochki += 1

    if q3 == "Германия":
        tochki += 1

    if q4 == "Владимир Ленин":
        tochki += 1

    if q5 == "1939":
        tochki += 1

    st.write(f" Резултат е: {tochki} / 5")
