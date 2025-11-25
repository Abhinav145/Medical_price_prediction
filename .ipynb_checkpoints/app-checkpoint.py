{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1092e874-6a23-483c-8d99-c7ea901b2933",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load the model\n",
    "pipe = pickle.load(open('pipe.pkl', 'rb'))\n",
    "\n",
    "st.set_page_config(page_title=\"Medical Cost Prediction\", page_icon=\"💉\", layout=\"centered\")\n",
    "\n",
    "st.markdown(\"<h1 style='text-align: center; color: #4CAF50;'>💉 Medical Insurance Cost Predictor</h1>\", unsafe_allow_html=True)\n",
    "st.write(\"### Enter Patient Details\")\n",
    "\n",
    "col1, col2 = st.columns(2)\n",
    "\n",
    "with col1:\n",
    "    age = st.number_input(\"Age\", min_value=1, max_value=100, value=30)\n",
    "    bmi = st.number_input(\"BMI\", min_value=10.0, max_value=60.0, value=25.0)\n",
    "    children = st.number_input(\"Number of Children\", min_value=0, max_value=10, value=0)\n",
    "\n",
    "with col2:\n",
    "    sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "    smoker = st.selectbox(\"Smoker\", [\"yes\", \"no\"])\n",
    "    region = st.selectbox(\"Region\", [\"southwest\", \"southeast\", \"northwest\", \"northeast\"])\n",
    "\n",
    "if st.button(\"Predict Medical Charges\"):\n",
    "    input_data = np.array([[age, bmi, children, sex, smoker, region]])\n",
    "    prediction = pipe.predict(input_data)[0]\n",
    "\n",
    "    st.success(f\"### 💰 Estimated Medical Charges: **${prediction:,.2f}**\")\n",
    "    st.balloons()\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"<p style='text-align:center;'>Created by Abhinav — Powered by Machine Learning 🚀</p>\", unsafe_allow_html=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1b5dfdf-094b-4ee7-b5aa-72f4e5588a47",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
