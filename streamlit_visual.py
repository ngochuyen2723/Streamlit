import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def bai1():
    st.header("Bài 1: Vẽ đồ thị hàm số cơ bản")
    st.write("Chọn 1 trong các hàm số sin, cos, exp, log và vẽ biểu đồ trên đoạn [-10,10].")
    ham_so = st.selectbox("Chọn hàm số:",["sin", "cos","exp","log"])
    x = np.linspace(-10,10,100)
    match ham_so:
        case "sin":
            y = np.sin(x)
            ten_ham = "sin(x)"
        case "cos":
            y = np.cos(x)
            ten_ham = "cos(x)"
        case "exp":
            y = np.exp(x)
            ten_ham = "exp(x)"
        case "log":
            x = np.linspace(0.01,10,1000)
            y = np.log(x)
            ten_ham = "log(x)"
    fig = plt.figure(figsize=(10,6))
    plt.plot(x,y,'b-',linewidth = 2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Đồ thị hàm số y = {ten_ham}")
    plt.grid()
    st.pyplot(fig)

def bai2():
    st.header("Bài 2: So sánh 2 hàm số trên cùng 1 biểu đồ")
    st.write("Chọn hai hàm số bất kỳ trong số: sin, cos, exp, log, và vẽ chúng trên cùng một biểu đồ.")
    col1, col2 = st.columns(2)
    with col1:
        ham_1 = st.selectbox("Chọn hàm số thứ nhất:", ["sin","cos","sinh","cosh"])
    with col2:
        ham_2 = st.selectbox("Chọn hàm số thứ nhất:", ["cos","sin","cosh","sinh"])
    x = np.linspace(-10,10,1000)
    match ham_1:
        case "sin":
            y1 = np.sin(x)
            ten_ham1 = "sin(x)"
        case "cos":
            y1 = np.cos(x)
            ten_ham1 = "cos(x)"
        case "sinh":
            y1 = np.sinh(x)
            ten_ham1 = "sinh(x)"
        case "cosh":
            y1 = np.cosh(x)
            ten_ham1 = "cosh(x)"
    match ham_2:
        case "sin":
            y2 = np.sin(x)
            ten_ham2 = "sin(x)"
        case "cos":
            y2 = np.cos(x)
            ten_ham2 = "cos(x)"
        case "sinh":
            y2 = np.sinh(x)
            ten_ham2 = "sinh(x)"
        case "cosh":
            y2 = np.cosh(x)
            ten_ham2 = "cosh(x)"
    fig = plt.figure(figsize=(10,6))
    plt.plot(x,y1, 'b-',linewidth = 2, label = ten_ham1)
    plt.plot(x,y2, 'r-',linewidth = 2, label = ten_ham2)
    plt.title(f"So sánh đồ thị hàm số {ten_ham1} và {ten_ham2}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    st.pyplot(fig)

def bai3():
    st.header("Bài 3: Vẽ đồ thị hàm số bậc 2")
    st.write("Nhập hệ số a,b,c cho phương trình y = ax² + bx + c và vẽ đồ thị tương ứng")
    col1,col2,col3 = st.columns(3)
    with col1:
        a = st.number_input("Nhập hệ số a")
    with col2:
        b = st.number_input("Nhập hệ số b")
    with col3:
        c = st.number_input("Nhập hệ số c") 
    giaiptbac2(a,b,c)

def bai4():
    st.header("Bài 4: Tương tác với slider để khảo sát đồ thị")
    st.write("Dùng slider để điều chỉnh giá trị của a,b,c và cập nhật đồ thị theo thời gian thực")
    a = st.slider("Hệ số a:",min_value = -5.0, max_value = 5.0, value = 1.0,step = 0.1)
    b = st.slider("Hệ số b:",min_value = -10.0, max_value = 10.0, value = 1.0,step = 0.5)
    c = st.slider("Hệ số c:",min_value = -10.0, max_value = 10.0, value = 1.0,step = 0.5) 
    giaiptbac2(a,b,c)

def bai5():
    st.header("Bài 5: Vẽ Heatmap cho hàm z = x² + y²")
    st.write("Dùng seaborn.heatmap để vẽ biểu đồ nhiệt của hàm z = x² + y²")
    range_val = st.slider("Phạm vi giá trị x,y:", min_value = -10, max_value = 10, value = 5, step = 1)
    resolution = st.slider("Độ phân giải:",min_value = 10, max_value = 100, value = 50, step = 5)
    x = np.linspace(-range_val,range_val,resolution)
    y = np.linspace(-range_val,range_val,resolution)
    X,Y = np.meshgrid(x,y)
    Z = X**2 + Y**2
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Biều đồ 3D")
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title("Đồ thị hàm số z = x² + y²")
        fig.colorbar(surf, shrink = 0.5)
        plt.tight_layout()
        st.pyplot(fig)
    with col2:
        st.subheader("Biểu đồ nhiệt (Heatmap)")
        fig = plt.figure(figsize=(8, 6))
        sns.heatmap(Z, cmap="viridis", linewidth=0)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.xticks(rotation = 45)
        plt.yticks(rotation = 45)
        plt.title("Heatmap của hàm z = x² + y²")
        st.pyplot(fig)
    st.subheader("Đường đồng mức (Contour)")
    fig = plt.figure(figsize=(8, 6))
    contour = plt.contour(Z, cmap="viridis", levels = 15)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Đường đồng mức của hàm z = x² + y²")
    plt.clabel(contour, inline=True, fontsize=8)
    st.pyplot(fig)
    

def giaiptbac2(a,b,c):
    fig = plt.figure(figsize=(10,6))    
    if a != 0:
        x_dinh = -b/(2*a)
        y_dinh = a * x_dinh**2 + b * x_dinh + c
        plt.plot(x_dinh,y_dinh,'ro')
        if a > 0:
            st.write(f"Đường parabol hướng lên có điểm cực tiểu ({x_dinh},{y_dinh})")
        else:
            st.write(f"Đường parabol hướng xuống có điểm cực đại ({x_dinh},{y_dinh})")
        delta = b**2 - 4 * a * c
        if delta < 0:
            st.write(f"Phương trình {a}x² + {b}x + {c} = 0 vô nghiệm")
        elif delta == 0:
            st.write(f"Phương trình {a}x² + {b}x + {c} = 0 có nghiệm kép ({x_dinh},{y_dinh})")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            st.write(f"Phương trình {a}x² + {b}x + {c} = 0 có 2 nghiệm phân biệt tại x1 = {x1} và x2 = {x2}")
    x = np.linspace(locals().get('x_dinh', 0)-10,locals().get('x_dinh', 0)+10,1000)
    y = a * x**2 + b * x + c
    plt.plot(x,y,'g-',linewidth = 2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Đồ thị hàm số y = {a}x² + {b}x + {c}")
    plt.grid()
    st.pyplot(fig)
    

st.set_page_config(page_title = "Đồ thị hàm số",page_icon = "📊",layout="wide")
baitap_options = {
    1: "Bài 1: Vẽ đồ thị hàm số cơ bản",
    2: "Bài 2: So sánh 2 hàm số trên cùng một biểu đồ",
    3: "Bài 3: Vẽ đồ thị hàm số bậc 2",
    4: "Bài 4: Tương tác với slider để khảo sát đồ thị",
    5: "Bài 5: Vẽ Heatmap cho hàm z = x² + y²"}

st.title("Ứng dụng vẽ đồ thị hàm số")
bai_tap = st.sidebar.selectbox("Chọn bài tập:",options = [1,2,3,4,5],format_func=lambda x: baitap_options.get(x))
match bai_tap:
    case 1:
        bai1()
    case 2:
        bai2()
    case 3:
        bai3()
    case 4:
        bai4()
    case 5:
        bai5()

