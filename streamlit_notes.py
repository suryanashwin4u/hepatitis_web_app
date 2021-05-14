import streamlit as st
import pandas as pd
def main():

    st.text('show text function')
    st.markdown('_Markdown_') 
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.code('for i in range(8): foo()')
    
    df=pd.read_csv("data/clean_hepatitis_dataset.csv")
    st.dataframe(df)
    st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})

    st.line_chart(df)
    st.area_chart(df)
    st.bar_chart(df)
    st.pyplot(df)
    st.altair_chart(df)
    st.vega_lite_chart(df)
    st.plotly_chart(df)
    st.bokeh_chart(df)
    st.pydeck_chart(df)
    st.deck_gl_chart(df)
    st.graphviz_chart(df)
    st.map(df)

    st.image('./header.png')
    st.audio(data)
    st.video(data)

    st.button('Hit me')
    st.checkbox('Check me out')
    st.radio('Radio', [1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1,'2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.color_picker('Pick a color')

    for i in range(int(st.number_input('Num:'))): 
        foo()
    if st.sidebar.selectbox('I:',['f']) == 'f': 
        b()
    my_slider_val = st.slider('Quinn Mallory', 1, 88)
    st.write(slider_val)

    st.stop()

    st.beta_container()
    st.beta_columns(spec)
    col1, col2 = st.beta_columns(2)
    col1.subheader('Columnisation')
    st.beta_expander('Expander')
    with st.beta_expander('Expand'):
        st.write('Juicy deets')

    st.echo()
    with st.echo():
        st.write('Code will be executed and printed')

    st.progress(progress_variable_1_to_100)
    st.spinner()
    with st.spinner(text='In progress'):
            time.sleep(5)
    st.success('Done')
    st.balloons()
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')
    st.exception(e)

    st.empty()
    my_placeholder = st.empty()
    my_placeholder.text('Replaced!')
    st.help(pandas.DataFrame)
    st.get_option(key)
    st.set_option(key, value)
    st.set_page_config(layout='wide')

    DeltaGenerator.add_rows(data)
    my_table = st.table(df1)
    my_table.add_rows(df2)
    my_chart = st.line_chart(df1)
    my_chart.add_rows(df2)

    # @st.cache
    # >>> @st.cache
    # ... def foo(bar):
    # ...     # Mutate bar
    # ...     return data
    # >>> # Executes d1 as first time
    # >>> d1 = foo(ref1)
    # >>> # Does not execute d1; returns cached value, d1==d2
    # >>> d2 = foo(ref1)
    # >>> # Different arg, so function d1 executes
    # >>> d3 = foo(ref2)

if __name__=='__main__':

	#call main method
	main()
