
from msilib.schema import RadioButton
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import tkinter as tk
from ttkthemes import ThemedTk
from ttkthemes import THEMES
import math


root = Tk()
root.title('Coefficient of Friction Calculator')
###root.iconbitmap('Icon.ico')
root.geometry("530x512+300+150")


root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
alpha = 0
    

def maintab ():
    Main = Frame(root)
    Main.grid(row=0, column=0, sticky=NSEW)
    r = tk.IntVar()
    l1 = Label(Main, text="Choose support system: ").grid(row=0, column=0, sticky=W, pady=10, padx=10)
    r1 = Radiobutton(Main, text="Metal", variable=r, value=1, state=DISABLED).grid(row=1, column=0, sticky=W, pady=10, padx=30)
    r2 = Radiobutton(Main, text="Wood", variable=r, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30)
    r3 = Radiobutton(Main, text="Scaffolding", variable=r, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
    r4 = Radiobutton(Main, text="Precast Concrete", variable=r, value=4).grid(row=4, column=0, sticky=W, pady=10, padx=30)
    r5 = Radiobutton(Main, text="Concrete or Brick", variable=r, value=5).grid(row=5, column=0, sticky=W, pady=10, padx=30)
    r6 = Radiobutton(Main, text="Sharp Steel & Rock", variable=r, value=6).grid(row=6, column=0, sticky=W, pady=10, padx=30)
    r7 = Radiobutton(Main, text="Concrete Wall and Iron Beam Roof", variable=r, value=7).grid(row=7, column=0, sticky=W, pady=10, padx=30)
    r8 = Radiobutton(Main, text="No Support System", variable=r, value=8).grid(row=8, column=0, sticky=W, pady=10, padx=30)
        
    def nextstep_1():
        Main.destroy()
        if r.get() == 8:

            # NoSupporttab()
            def nosupport():
                NoSupport = Frame(root)
                NoSupport.grid(row=0, column=0, sticky=NSEW)
                ns = IntVar()
                Label(NoSupport, text='Type of ore:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                Radiobutton(NoSupport, text="Coal", variable=ns, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(NoSupport, text="Metal", variable=ns, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30)

                def next_ns_1():
                        NoSupport.destroy()
                        if ns.get() == 1:
                            NoSupportC = Frame(root)
                            NoSupportC.grid(row=0, column=0, sticky=NSEW)
                            nsc = IntVar()
                            Label(NoSupportC, text='Type of Mining:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(NoSupportC, text='Shortcut Tunnel in Rock', variable=nsc, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(NoSupportC, text='Extentension Tunnel in Rock', variable=nsc, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(NoSupportC, text='Trail Tunnel in Coal', variable=nsc, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(NoSupportC, text='Vent Tunnel in Coal', variable=nsc, value=4).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                            
                            def next_ns_2():
                                NoSupportC.destroy()
                                if nsc.get() == 1:
                                    NoSupportC1 = Frame(root)
                                    NoSupportC1.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportC1, text='α = 0.00010').grid(row=0, column=0, columnspan=2, pady=100, padx=10)
                                    Button(NoSupportC1, text='Start Over', command=maintab).place(x=30, y=450)
                                    NoSupportC1.tkraise()
                                elif nsc.get() == 2:
                                    NoSupportC2 = Frame(root)
                                    NoSupportC2.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportC2, text='α = 0.0008').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(NoSupportC2, text='Start Over', command=maintab).place(x=30, y=450) 
                                    NoSupportC2.tkraise()
                                elif nsc.get() == 3:
                                    NoSupportC3 = Frame(root)
                                    NoSupportC3.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportC3, text='α = 0.0005-0.0008').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(NoSupportC3, text='Start Over', command=maintab).place(x=30, y=450) 
                                    NoSupportC3.tkraise()
                                elif nsc.get() == 4:
                                    NoSupportC4 = Frame(root)
                                    NoSupportC4.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportC4, text='α = 0.0008').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(NoSupportC4, text='Start Over', command=maintab).place(x=30, y=450) 
                                    NoSupportC4.tkraise()
                                    
                            bnsc1 = Button(NoSupportC, text='Next', command=next_ns_2).place(x=405, y=450) 
                            bnsc2 = Button(NoSupportC, text='Start Over', command=maintab).place(x=30, y=450)
                            NoSupportC.tkraise()
                            
                        elif ns.get() == 2:
                            NoSupport.destroy()
                            NoSupportM = Frame(root)
                            NoSupportM.grid(row=0, column=0, sticky=NSEW)
                            nsm = IntVar()
                            Label(NoSupportM, text='Type of Mining:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(NoSupportM, text='Extension Air Vent', variable=nsm, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(NoSupportM, text='Perpendicular Air Vent', variable=nsm, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(NoSupportM, text='Slope Air Vent', variable=nsm, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                            
                            def next_ns_3():
                                NoSupportM.destroy()
                                if nsm.get() == 1:
                                    NoSupportM1 = Frame(root)
                                    NoSupportM1.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportM1, text='α = 0.0010 - 0.0012').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(NoSupportM1, text='Start Over', command=maintab).place(x=30, y=450)
                                    NoSupportM1.tkraise()
                                elif nsm.get() == 2:
                                    NoSupportM2 = Frame(root)
                                    NoSupportM2.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportM2, text='α = 0.0013 - 0.0017').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(NoSupportM2, text='Start Over', command=maintab).place(x=375, y=450)
                                    NoSupportM.tkraise()

                                elif nsm.get() == 3:
                                    NoSupportM3 = Frame(root)
                                    NoSupportM3.grid(row=0, column=0, sticky=NSEW)
                                    Label(NoSupportM3, text='α = 0.0020 - 0.0022').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(NoSupportM3, text='Start Over', command=maintab).place(x=30, y=450)
                            Button(NoSupportM, text='Next', command=next_ns_3).place(x=405, y=450)
                            Button(NoSupportM, text='Start Over', command=maintab).place(x=30, y=450)
                            NoSupportM.tkraise()

                Button(NoSupport, text='Next', command= next_ns_1).place(x=375, y=450)
                Button(NoSupport, text='Start Over', command=maintab).place(x=30, y=450)
                NoSupport.tkraise()
            nosupport()
        elif r.get() == 7:
            #Concrete Wall and Iron Beam Roof
            
            def cw_gr():
                cwgr = Frame(root)
                cwgr.grid(row=0, column=0, sticky=NSEW)
                cg1 = StringVar()
                cg2 = StringVar()
                Label(cwgr, text='Iron Beam Number: ').grid(row=0, column=0, sticky=W, padx=10, pady=10)
                OptionMenu(cwgr, cg1, " ","12", "14", "16", "18").grid(row=0, column=1, padx=10, pady=10)
                Label(cwgr, text='Length/Diameter: ').grid(row=1, column=0, sticky=W, padx=10, pady=10)
                OptionMenu(cwgr, cg2, "", "2", "3", "5", "6", "8").grid(row=1, column=1, padx=10, pady=10)
                cg1.set("Select...")
                cg2.set("Select...")
                
                def next_cg():
                    if int(cg1.get()) == 12:
                        if int(cg2.get()) == 2:
                            ci1 = Frame(root)
                            ci1.grid(row=0, column=0, sticky=NSEW)
                            Label(ci1, text='α = 0.000715').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci1, text='Start Over', command=maintab).place(x=30, y=450)
                            ci1.tkraise()
                        elif int(cg2.get()) == 3:
                            ci2 = Frame(root)
                            ci2.grid(row=0, column=0, sticky=NSEW)
                            Label(ci2, text='α = 0.0008').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci2, text='Start Over', command=maintab).place(x=30, y=450)
                            ci2.tkraise()
                        elif int(cg2.get()) == 5:
                            ci3 = Frame(root)
                            ci3.grid(row=0, column=0, sticky=NSEW)
                            Label(ci3, text='α = 0.00088').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci3, text='Start Over', command=maintab).place(x=30, y=450)
                            ci3.tkraise()
                        elif int(cg2.get()) == 6:
                            ci4 = Frame(root)
                            ci4.grid(row=0, column=0, sticky=NSEW)
                            Label(ci4, text='α = 0.00092').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci4, text='Start Over', command=maintab).place(x=30, y=450)
                            ci4.tkraise()
                        elif int(cg2.get()) == 8:
                            ci5 = Frame(root)
                            ci5.grid(row=0, column=0, sticky=NSEW)
                            Label(ci5, text='α = 0.0009').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci5, text='Start Over', command=maintab).place(x=30, y=450)
                            ci5.tkraise()
                    elif int(cg1.get()) == 14:
                        if int(cg2.get()) == 2:
                            ci6 = Frame(root)
                            ci6.grid(row=0, column=0, sticky=NSEW)
                            Label(ci6, text='α = 0.00077').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci6, text='Start Over', command=maintab).place(x=30, y=450)
                            ci6.tkraise()
                        elif int(cg2.get()) == 3:
                            ci7 = Frame(root)
                            ci7.grid(row=0, column=0, sticky=NSEW)
                            Label(ci7, text='α = 0.00082').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci7, text='Start Over', command=maintab).place(x=30, y=450)
                            ci7.tkraise()
                        elif int(cg2.get()) == 5:
                            ci8 = Frame(root)
                            ci8.grid(row=0, column=0, sticky=NSEW)
                            Label(ci8, text='α = 0.00091').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci8, text='Start Over', command=maintab).place(x=30, y=450)
                            ci8.tkraise()
                        elif int(cg2.get()) == 6:
                            ci9 = Frame(root)
                            ci9.grid(row=0, column=0, sticky=NSEW)
                            Label(ci9, text='α = 0.00095').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci9, text='Start Over', command=maintab).place(x=30, y=450)
                            ci9.tkraise()
                        elif int(cg2.get()) == 8:
                            ci10 = Frame(root)
                            ci10.grid(row=0, column=0, sticky=NSEW)
                            Label(ci10, text='α = 0.00093').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci10, text='Start Over', command=maintab).place(x=30, y=450)
                            ci10.tkraise()
                    elif int(cg1.get()) == 16:
                        if int(cg2.get()) == 2:
                            ci11 = Frame(root)
                            ci11.grid(row=0, column=0, sticky=NSEW)
                            Label(ci11, text='α = 0.00078').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci11, text='Start Over', command=maintab).place(x=30, y=450)
                            ci11.tkraise()
                        elif int(cg2.get()) == 3:
                            ci12 = Frame(root)
                            ci12.grid(row=0, column=0, sticky=NSEW)
                            Label(ci12, text='α = 0.00084').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci12, text='Start Over', command=maintab).place(x=30, y=450)
                            ci12.tkraise()
                        elif int(cg2.get()) == 5:
                            ci13 = Frame(root)
                            ci13.grid(row=0, column=0, sticky=NSEW)
                            Label(ci13, text='α = 0.00093').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci13, text='Start Over', command=maintab).place(x=30, y=450)
                            ci13.tkraise()
                        elif int(cg2.get()) == 6:
                            ci14 = Frame(root)
                            ci14.grid(row=0, column=0, sticky=NSEW)
                            Label(ci14, text='α = 0.00097').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci14, text='Start Over', command=maintab).place(x=30, y=450)
                            ci14.tkraise()
                        elif int(cg2.get()) == 8:
                            ci15 = Frame(root)
                            ci15.grid(row=0, column=0, sticky=NSEW)
                            Label(ci15, text='α = 0.00095').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci15, text='Start Over', command=maintab).place(x=30, y=450)
                            ci15.tkraise()
                    elif int(cg1.get()) == 18:
                        if int(cg2.get()) == 2:
                            ci16 = Frame(root)
                            ci16.grid(row=0, column=0, sticky=NSEW)
                            Label(ci16, text='α = 0.0008').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci16, text='Start Over', command=maintab).place(x=30, y=450)
                            ci16.tkraise()
                        elif int(cg2.get()) == 3:
                            ci17 = Frame(root)
                            ci17.grid(row=0, column=0, sticky=NSEW)
                            Label(ci17, text='α = 0.00085').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci17, text='Start Over', command=maintab).place(x=30, y=450)
                            ci17.tkraise()
                        elif int(cg2.get()) == 5:
                            ci18 = Frame(root)
                            ci18.grid(row=0, column=0, sticky=NSEW)
                            Label(ci18, text='α = 0.00095').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci18, text='Start Over', command=maintab).place(x=30, y=450)
                            ci18.tkraise()
                        elif int(cg2.get()) == 6:
                            ci19 = Frame(root)
                            ci19.grid(row=0, column=0, sticky=NSEW)
                            Label(ci19, text='α = 0.0010').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci19, text='Start Over', command=maintab).place(x=30, y=450)
                            ci19.tkraise()
                        elif int(cg2.get()) == 8:
                            ci20 = Frame(root)
                            ci20.grid(row=0, column=0, sticky=NSEW)
                            Label(ci20, text='α = 0.00098').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ci20, text='Start Over', command=maintab).place(x=30, y=450)
                            ci20.tkraise()
                
                Button(cwgr, text='Next', command= next_cg).place(x=405, y=450)
                Button(cwgr, text='Start Over', command=maintab).place(x=30, y=450)
                cwgr.tkraise()
            
            cw_gr()
        elif r.get() == 6:
            #Sharp Steel & Rock
            
            def ssr():
                sr = Frame(root)
                sr.grid(row=0, column=0, sticky=NSEW)
                sr1 = StringVar()
                sr2 = StringVar()
                Label(sr, text='Length of the side of the rock square: ').grid(row=0, column=0, sticky=W, padx=10, pady=10)
                OptionMenu(sr, sr1, "", "40", "50").grid(row=0, column=1, padx=10, pady=10)
                Label(sr, text='Length/Diameter: ').grid(row=1, column=0, sticky=W, padx=10, pady=10)
                OptionMenu(sr, sr2,"", "2", "3").grid(row=1, column=1, padx=10, pady=10)
                sr1.set("Select..")
                sr2.set("Select...")
                
                def next_sr():
                    if int(sr1.get()) == 40:
                        if int(sr2.get()) == 2:
                            ssr1 = Frame(root)
                            ssr1.grid(row=0, column=0, sticky=NSEW)
                            Label(ssr1, text='α = 0.0021').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ssr1, text='Start Over', command=maintab).place(x=30, y=450)
                            ssr1.tkraise()
                        elif int(sr2.get()) == 3:
                            ssr2 = Frame(root)
                            ssr2.grid(row=0, column=0, sticky=NSEW)
                            Label(ssr2, text='α = 0.0026').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ssr2, text='Start Over', command=maintab).place(x=30, y=450)
                            ssr2.tkraise()
                    elif int(sr1.get()) == 50:
                        if int(sr2.get()) == 2:
                            ssr3 = Frame(root)
                            ssr3.grid(row=0, column=0, sticky=NSEW)
                            Label(ssr3, text='α = 0.0027').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ssr3, text='Start Over', command=maintab).place(x=30, y=450)
                            ssr3.tkraise()
                        elif int(sr2.get()) == 3:
                            ssr4 = Frame(root)
                            ssr4.grid(row=0, column=0, sticky=NSEW)
                            Label(ssr4, text='α = 0.0026').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                            Button(ssr4, text='Start Over', command=maintab).place(x=30, y=450)
                            ssr4.tkraise()
                    
                Button(sr, text='Next', command= next_sr).place(x=405, y=450)
                Button(sr, text='Start Over', command=maintab).place(x=30, y=450)
                sr.tkraise()
            ssr()
        elif r.get() == 5:
            #Concrete or Brick
            def cob():
                cb = Frame(root)
                cb.grid(row=0, column=0, sticky=NSEW)
                cbv = DoubleVar()
                Label(cb, text='Type of Area:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                Radiobutton(cb, text='Circular', variable=cbv, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(cb, text='Non-Circular', variable=cbv, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30)
                def next_cob():
                    if cbv.get() == 1:
                        circular = Frame(root)
                        circvar = DoubleVar()
                        circular.grid(row=0, column=0, sticky=NSEW)
                        Label(circular, text='Type of cover:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                        Radiobutton(circular, text="Smooth Concrete", variable=circvar, value=0.00025).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(circular, text="Rough Concrete", variable=circvar, value=0.00070).grid(row=2, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(circular, text="Bricklaying", variable=circvar, value=0.00130).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(circular, text="Rock Cover", variable=circvar, value=0.00800).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(circular, text="Rough Rock Cover", variable=circvar, value=0.02000).grid(row=5, column=0, sticky=W, pady=10, padx=30)
                        def next_circular():
                            solution = Frame(root)
                            solution.grid(row=0, column=0, sticky=NSEW)
                            Label(solution, text="Enter the diameter:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            D = Entry(solution)
                            D.grid(row=0, column=1, padx=10, pady=10)
                            def getresult():
                                result = Frame(root)
                                result.grid(row=0, column=0, sticky=NSEW)
                                d_value = float(D.get())
                                d0_value = float(circvar.get())
                                numerator = 0.015
                                denominator = ((1.74 + 2 * math.log10(d_value / d0_value)) ** 2)
                                alpha = numerator / denominator
                                Label(result, text=f"α = {alpha:.8f}").grid(row=0, column=0, sticky="W", pady=100, padx=10)
                                result.tkraise()
                                Button(solution, text='Start Over', command=maintab).place(x=30, y=450)
                            solution.tkraise()
                            Button(solution, text='Next', command=getresult).place(x=405, y=450)
                            Button(solution, text='Start Over', command=maintab).place(x=30, y=450)
                        Button(circular, text='Next', command=next_circular).place(x=405, y=450)
                        Button(circular, text='Start Over', command=maintab).place(x=30, y=450)
                        circular.tkraise()
                    if cbv.get() == 2:
                        noncircular = Frame(root)
                        noncircvar = DoubleVar()
                        noncircular.grid(row=0, column=0, sticky=NSEW)
                        Label(noncircular, text='Type of cover:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                        Radiobutton(noncircular, text="Smooth Concrete", variable=noncircvar, value=0.00025).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(noncircular, text="Rough Concrete", variable=noncircvar, value=0.00070).grid(row=2, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(noncircular, text="Bricklaying", variable=noncircvar, value=0.00130).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(noncircular, text="Rock Cover", variable=noncircvar, value=0.00800).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                        Radiobutton(noncircular, text="Rough Rock Cover", variable=noncircvar, value=0.02000).grid(row=5, column=0, sticky=W, pady=10, padx=30)
                        def next_noncircular():
                            solution = Frame(root)
                            solution.grid(row=0, column=0, sticky=NSEW)
                            Label(solution, text="Enter the Surface Area:").grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            D = Entry(solution)
                            D.grid(row=0, column=1, padx=10, pady=10)
                            def getresult():
                                result = Frame(root)
                                result.grid(row=0, column=0, sticky=NSEW)
                                d_value = float(D.get())
                                d0_value = float(noncircvar.get())
                                numerator = 0.015
                                denominator = (1.74 +  16.3 * math.log10((4.8 * (math.sqrt(d_value))) / d0_value)) ** 2
                                alpha = numerator / denominator
                                Label(result, text=f"α = {alpha:.8f}").grid(row=0, column=0, sticky="W", pady=100, padx=10)
                                result.tkraise()
                                Button(solution, text='Start Over', command=maintab).place(x=30, y=450)
                            solution.tkraise()
                            Button(solution, text='Next', command=getresult).place(x=405, y=450)
                            Button(solution, text='Start Over', command=maintab).place(x=30, y=450)
                        Button(noncircular, text='Next', command=next_noncircular).place(x=405, y=450)
                        Button(noncircular, text='Start Over', command=maintab).place(x=30, y=450)
                        noncircular.tkraise()
                next_cob()
                Button(cb, text='Next', command=next_cob).place(x=405, y=450)
                Button(cb, text='Start Over', command=maintab).place(x=30, y=450)

                cb.tkraise()
            cob()

        elif r.get() == 4:
            def precast():
                pc = Frame(root)
                pc.grid(row=0, column=0, sticky=NSEW)
                pcv = IntVar()
                Label(pc, text='Type of Support:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                Radiobutton(pc, text="Concrete frames, made up of base and column\nwith a rectangular cross section\nand fixed connection on both ends", variable=pcv, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(pc, text="Concrete frames, made up of base and column\nwith a 'T' cross section and fixed\nconnection on both ends", variable=pcv, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                Radiobutton(pc, text="Concrete frames, made up of base and column\nwith a 'T' cross section and a\ncentral base", variable=pcv, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(pc, text='Concrete frame made up of four joints', variable=pcv, value=4).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(pc, text='Polygonal concrete frame', variable=pcv, value=5).grid(row=5, column=0, sticky=W, pady=10, padx=30)

                def next_pc1():
                    if pcv.get() == 1:
                        pc.destroy()
                        def precast1():
                            pc1 = Frame(root)
                            pc1.grid(row=0, column=0, sticky=NSEW)
                            pcv1 = IntVar()
                            Label(pc1, text='Distance between two frames:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(pc1, text="0.55 m", variable=pcv1, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc1, text="0.75 m", variable=pcv1, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(pc1, text="1 m", variable=pcv1, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc1, text='1.14 m', variable=pcv1, value=4).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc1, text='1.34 m', variable=pcv1, value=5).grid(row=5, column=0, sticky=W, pady=10, padx=30)
                            def n1():
                                if pcv1.get() == 1:
                                    pc55 = Frame(root)
                                    pc55.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc55, text='α = 0.0011').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc55, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc55.tkraise()
                                elif pcv1.get() == 2:
                                    pc75 = Frame(root)
                                    pc75.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc75, text='α = 0.0013').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc75, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc75.tkraise()
                                elif pcv1.get() == 3:
                                    pc_1 = Frame(root)
                                    pc_1.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc_1, text='α = 0.0021').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc_1, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc_1.tkraise()
                                elif pcv1.get() == 4:
                                    pc114 = Frame(root)
                                    pc114.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc114, text='α = 0.0019').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc114, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc114.tkraise()
                                elif pcv1.get() == 5:
                                    pc134 = Frame(root)
                                    pc134.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc134, text='α = 0.0018').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc134, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc134.tkraise()
                            Button(pc1, text='Next', command=n1).place(x=405, y=450)
                            Button(pc1, text='Start Over', command=maintab).place(x=30, y=450)
                            pc1.tkraise()
                        precast1()
                    elif pcv.get() == 2:
                        pc.destroy()
                        def precast2():
                            pc2 = Frame(root)
                            pc2.grid(row=0, column=0, sticky=NSEW)
                            pcv2 = IntVar()
                            Label(pc2, text='Distance between two frames:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(pc2, text="0.94 m", variable=pcv2, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc2, text="1.14 m", variable=pcv2, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(pc2, text="1.34 m", variable=pcv2, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                            def n2():
                                if pcv2.get() == 1:
                                    pc94 = Frame(root)
                                    pc94.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc94, text='α = 0.0009').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc94, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc94.tkraise()
                                elif pcv2.get() == 2:
                                    pc114 = Frame(root)
                                    pc114.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc114, text='α = 0.0009').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc114, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc114.tkraise()
                                elif pcv2.get() == 3:
                                    pc134 = Frame(root)
                                    pc134.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc134, text='α = 0.0007').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc134, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc134.tkraise()
                            Button(pc2, text='Next', command=n2).place(x=405, y=450)
                            Button(pc2, text='Start Over', command=maintab).place(x=30, y=450)
                            pc2.tkraise()
                        precast2()
                    elif pcv.get() == 3:
                        pc.destroy()
                        def precast3():
                            pc3 = Frame(root)
                            pc3.grid(row=0, column=0, sticky=NSEW)
                            pcv3 = IntVar()
                            Label(pc3, text='Distance between two frames:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(pc3, text="1.14 m", variable=pcv3, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(pc3, text="1.34 m", variable=pcv3, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30)
                            def n3():
                                if pcv3.get() == 1:
                                    pc114 = Frame(root)
                                    pc114.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc114, text='α = 0.0023').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc114, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc114.tkraise()
                                elif pcv3.get() == 2:
                                    pc134 = Frame(root)
                                    pc134.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc134, text='α = 0.0022').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc134, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc134.tkraise()
                            Button(pc3, text='Next', command=n3).place(x=405, y=450)
                            Button(pc3, text='Start Over', command=maintab).place(x=30, y=450)
                            pc3.tkraise()
                        precast3()
                    elif pcv.get() == 4:
                        pc.destroy()
                        def precast4():
                            pc4 = Frame(root)
                            pc4.grid(row=0, column=0, sticky=NSEW)
                            pcv4 = IntVar()
                            Label(pc4, text='Distance between two frames:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(pc4, text="0.32 m", variable=pcv4, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc4, text="0.50 m", variable=pcv4, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(pc4, text="0.64 m", variable=pcv4, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc4, text="1 m", variable=pcv4, value=4).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                            def n4():
                                if pcv4.get() == 1:
                                    pc32 = Frame(root)
                                    pc32.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc32, text='α = 0.00107').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc32, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc32.tkraise()
                                elif pcv4.get() == 2:
                                    pc50 = Frame(root)
                                    pc50.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc50, text='α = 0.0014').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc50, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc50.tkraise()
                                elif pcv4.get() == 3:
                                    pc64 = Frame(root)
                                    pc64.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc64, text='α = 0.00174').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc64, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc64.tkraise()
                                elif pcv4.get() == 4:
                                    pc_1 = Frame(root)
                                    pc_1.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc_1, text='α = 0.0019').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc_1, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc_1.tkraise()
                            Button(pc4, text='Next', command=n4).place(x=405, y=450)
                            Button(pc4, text='Start Over', command=maintab).place(x=30, y=450)
                            pc4.tkraise()
                        precast4()
                    elif pcv.get() == 5:
                        pc.destroy()
                        def precast5():
                            pc5 = Frame(root)
                            pc5.grid(row=0, column=0, sticky=NSEW)
                            pcv5 = IntVar()
                            Label(pc5, text='Distance between two frames:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                            Radiobutton(pc5, text="0.32 m", variable=pcv5, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc5, text="0.50 m", variable=pcv5, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30) 
                            Radiobutton(pc5, text="0.64 m", variable=pcv5, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                            Radiobutton(pc5, text="1 m", variable=pcv5, value=4).grid(row=4, column=0, sticky=W, pady=10, padx=30)
                            def n5():
                                if pcv5.get() == 1:
                                    pc_32 = Frame(root)
                                    pc_32.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc_32, text='α = 0.0010').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc_32, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc_32.tkraise()
                                elif pcv5.get() == 2:
                                    pc_50 = Frame(root)
                                    pc_50.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc_50, text='α = 0.00125').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc_50, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc_50.tkraise()
                                elif pcv5.get() == 3:
                                    pc_64 = Frame(root)
                                    pc_64.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc_64, text='α = 0.0013').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc_64, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc_64.tkraise()
                                elif pcv5.get() == 4:
                                    pc_11 = Frame(root)
                                    pc_11.grid(row=0, column=0, sticky=NSEW)
                                    Label(pc_11, text='α = 0.00165').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(pc_11, text='Start Over', command=maintab).place(x=30, y=450)
                                    pc_11.tkraise()
                            Button(pc5, text='Next', command=n5).place(x=405, y=450)
                            Button(pc5, text='Start Over', command=maintab).place(x=30, y=450)
                            pc5.tkraise()
                        precast5()
                Button(pc, text='Next', command=next_pc1).place(x=405, y=450)
                Button(pc, text='Start Over', command=maintab).place(x=30, y=450)
                pc.tkraise()
                
            precast()
        
        elif r.get() == 3:
            def scaffolding():
                sc = Frame(root)
                sc.grid(row=0, column=0, sticky=NSEW)
                scv = IntVar()
                Label(sc, text='Does it have Reinforcement Pillars?').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                Radiobutton(sc, text="Yes", variable=scv, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(sc, text="No", variable=scv, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30)
                def next_scaffolding1():
                    if scv.get() == 1:
                        scr = Frame(root)
                        scr.grid(row=0, column=0, sticky=NSEW)
                        sc1 = StringVar()
                        sc2 = StringVar()
                        sc3 = StringVar()
                        Label(scr, text='Diameter of the woods (In cm): ').grid(row=0, column=0, sticky=W, padx=10, pady=10)
                        OptionMenu(scr, sc1, "", "18", "20", "24").grid(row=0, column=1, padx=10, pady=10)
                        Label(scr, text='Length/Diameter: ').grid(row=1, column=0, sticky=W, padx=10, pady=10)
                        OptionMenu(scr, sc2, "", "4", "6", "8").grid(row=1, column=1, padx=10, pady=10)
                        Label(scr, text='Surface area: ').grid(row=2, column=0, sticky=W, padx=10, pady=10)
                        OptionMenu(scr, sc3, "", "4", "6").grid(row=2, column=1, padx=10, pady=10)
                        sc1.set("Select..")
                        sc2.set("Select...")
                        sc3.set("Select...")
                        def next_scaffolding2():
                            if int(sc3.get()) == 4:
                                if int(sc1.get()) == 18:
                                    if int(sc2.get()) == 4:
                                        scr1 = Frame(root)
                                        scr1.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr1, text='α = 0.0043').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr1, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 6:
                                        scr2 = Frame(root)
                                        scr2.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr2, text='α = 0.0040').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr2, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 8:
                                        scr3 = Frame(root)
                                        scr3.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr3, text='α = 0.0037').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr3, text='Start Over', command=maintab).place(x=30, y=450)
                                elif int(sc1.get()) == 20:
                                    if int(sc2.get()) == 4:
                                        scr4 = Frame(root)
                                        scr4.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr4, text='α = 0.0044').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr4, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 6:
                                        scr5 = Frame(root)
                                        scr5.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr5, text='α = 0.0041').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr5, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 8:
                                        scr6 = Frame(root)
                                        scr6.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr6, text='α = 0.0039').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr6, text='Start Over', command=maintab).place(x=30, y=450)
                                if int(sc1.get()) == 24:
                                    if int(sc2.get()) == 4:
                                        scr7 = Frame(root)
                                        scr7.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr7, text='α = 0.0046').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr7, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 6:
                                        scr8 = Frame(root)
                                        scr8.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr8, text='α = 0.0043').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr8, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 8:
                                        scr9 = Frame(root)
                                        scr9.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr9, text='α = 0.0040').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr9, text='Start Over', command=maintab).place(x=30, y=450)
                            elif int(sc3.get()) == 6:
                                if int(sc1.get()) == 18:
                                    if int(sc2.get()) == 4:
                                        scr1 = Frame(root)
                                        scr1.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr1, text='α = 0.0040').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr1, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 6:
                                        scr2 = Frame(root)
                                        scr2.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr2, text='α = 0.0037').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr2, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 8:
                                        scr3 = Frame(root)
                                        scr3.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr3, text='α = 0.0034').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr3, text='Start Over', command=maintab).place(x=30, y=450)
                                elif int(sc1.get()) == 20:
                                    if int(sc2.get()) == 4:
                                        scr4 = Frame(root)
                                        scr4.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr4, text='α = 0.0041').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr4, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 6:
                                        scr5 = Frame(root)
                                        scr5.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr5, text='α = 0.0038').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr5, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 8:
                                        scr6 = Frame(root)
                                        scr6.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr6, text='α = 0.0036').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr6, text='Start Over', command=maintab).place(x=30, y=450)
                                if int(sc1.get()) == 24:
                                    if int(sc2.get()) == 4:
                                        scr7 = Frame(root)
                                        scr7.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr7, text='α = 0.0043').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr7, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 6:
                                        scr8 = Frame(root)
                                        scr8.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr8, text='α = 0.0040').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr8, text='Start Over', command=maintab).place(x=30, y=450)
                                    elif int(sc2.get()) == 8:
                                        scr9 = Frame(root)
                                        scr9.grid(row=0, column=0, sticky=NSEW)
                                        Label(scr9, text='α = 0.0037').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                        Button(scr9, text='Start Over', command=maintab).place(x=30, y=450)
                        Button(scr, text='Next', command=next_scaffolding2).place(x=405, y=450)
                        Button(scr, text='Start Over', command=maintab).place(x=30, y=450)
                        scr.tkraise()
                    elif scv.get() == 2:
                        sc10 = Frame(root)
                        sc10.grid(row=0, column=0, sticky=NSEW)
                        Label(sc10, text='α = 0.0063').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                        Button(sc10, text="Start Over", command=maintab).place(x=30, y=450)
                        sc10.tkraise()
                        
                 
                bsc1 = Button(sc, text='Next', command=next_scaffolding1).place(x=405, y=450)
                bsc2 = Button(sc, text='Start Over', command=maintab).place(x=30, y=450)
                sc.tkraise()
            scaffolding()  
        
        elif r.get() == 2:
            wdv = IntVar()
            def wood():
                wd = Frame(root)
                wd.grid(row=0, column=0, sticky=NSEW)
                Label(wd, text='How many wooden pillars are used?').grid(row=0, column=0, sticky=W, pady=10, padx=10)
                Radiobutton(wd, text="Three", variable=wdv, value=1).grid(row=1, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(wd, text="Four", variable=wdv, value=2).grid(row=2, column=0, sticky=W, pady=10, padx=30)
                Radiobutton(wd, text="Other", variable=wdv, value=3).grid(row=3, column=0, sticky=W, pady=10, padx=30)
                wd.tkraise()
                
                def next_wd():
                    if wdv.get() == 3:
                        voronin = Frame(root)
                        voronin.grid(row=0, column=0, sticky=NSEW)
                        Label(voronin, text="What is the mining area? ").grid(row=0, column=0, padx=10, pady=10)
                        S = Entry(voronin)
                        S.grid(row=0, column=1, padx=10, pady=10)
                        Label(voronin, text="What is the diameter of woods? ").grid(row=1, column=0, padx=10, pady=10)
                        d = Entry(voronin)
                        d.grid(row=1, column=1, padx=10, pady=10)
                        Label(voronin, text="What is the distance between two consecutive frames? ").grid(row=2, column=0, padx=10, pady=10)
                        l = Entry(voronin)
                        l.grid(row=2, column=1, padx=10, pady=10)
                        Label(voronin, text="What is the the ratio of the fixed wood part to \nthe mineral working environment? ").grid(row=3, column=0, padx=10, pady=10)
                        m2 = Entry(voronin)
                        m2.grid(row=3, column=1, padx=10, pady=10)
                        def next_voronin():
                            nvoronin = Frame(root)
                            nvoronin.grid(row=0, column=0, sticky=NSEW)
                            S_value = float(S.get())  
                            d_value = float(d.get())  
                            epsilon = 0.48 * math.sqrt(S_value) / d_value
                            Label(nvoronin, text=f"α = {epsilon:.2f}").grid(row=0, column=0, sticky="W", pady=100, padx=10)
                            Button(nvoronin, text="Start Over", command=maintab).place(x=30, y=450)
                            nvoronin.tkraise()  
                        Button(voronin, text="Next", command=next_voronin).place(x=405, y=450)
                        Button(voronin, text="Start Over", command=maintab).place(x=30, y=450)
                        voronin.tkraise()
                    elif wdv.get() == 1:
                        wd.destroy()
                        wd1 = Frame(root)
                        wd1.grid(row=0, column=0, sticky=NSEW)
                        wdv1 = StringVar()
                        wdv2 = StringVar()
                        Label(wd1, text='Diameter of wood pillar: ').grid(row=0, column=0, padx=10, pady=10)
                        OptionMenu(wd1, wdv1,"", "15", "16", "17", "18", "20", "22", "24", "28", "Other").grid(row=0, column=1, padx=10, pady=10)
                        Label(wd1, text='Length/Diameter: ').grid(row=1, column=0, padx=10, pady=10)
                        OptionMenu(wd1, wdv2,"", "1", "2", "3", "4", "5", "6", "Other").grid(row=1, column=1, padx=10, pady=10)
                        wdv1.set("Select..")
                        wdv2.set("Select...")
                        wd1.tkraise()
                        def next_wd1():
                            if wdv1.get() == "Other" or wdv2.get() == "Other":
                                wdf = Frame(root)
                                wdf.grid(row=1, column=0, sticky=NSEW)
                                wdf.tkraise()
                            elif int(wdv1.get()) == 15:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00107').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00128').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00155').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00160').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00155').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00148').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 16:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00111').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00132').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00158').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00162').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00159').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00151').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 17:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00114').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00136').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00161').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00166').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00161').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00154').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 18:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00118').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00140').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00164').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00169').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00164').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00157').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 20:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00126').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00148').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00172').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00177').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00172').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00165').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 22:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00134').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00165').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00180').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00185').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00180').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00173').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 24:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00140').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00162').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00186').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00192').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00186').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00179').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 28:
                                if int(wdv2.get()) == 1:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00150').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00177').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00202').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00207').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00202').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00195').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                        Button(wd1, text='Next', command=next_wd1).place(x=405, y=450)
                        Button(wd1, text='Start Over', command=maintab).place(x=30, y=450)
                    elif wdv.get() == 2:
                        wd.destroy()
                        wd1 = Frame(root)
                        wd1.grid(row=0, column=0, sticky=NSEW)
                        wdv1 = StringVar()
                        wdv2 = StringVar()
                        Label(wd1, text='Diameter of wood pillar: ').grid(row=0, column=0, padx=10, pady=10)
                        OptionMenu(wd1, wdv1,"", "15", "17", "20", "22", "Other").grid(row=0, column=1, padx=10, pady=10)
                        Label(wd1, text='Length/Diameter: ').grid(row=1, column=0, padx=10, pady=10)
                        OptionMenu(wd1, wdv2,"", "2", "3", "4", "5", "6", "8", "Other").grid(row=1, column=1, padx=10, pady=10)
                        wdv1.set("Select..")
                        wdv2.set("Select...")
                        wd1.tkraise()
                        def next_wd2():
                            if wdv1.get() == "Other" or wdv2.get() == "Other":
                                wdf = Frame(root)
                                wdf.grid(row=1, column=0, sticky=NSEW)
                                wdf.tkraise()
                            elif int(wdv1.get()) == 15:
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00114').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00165').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00190').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00209').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00226').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 8:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00210').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 17:
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00150').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00176').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00200').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00220').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00239').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 8:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00225').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 20:
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00159').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00187').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00212').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00235').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00256').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 8:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00240').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                            elif int(wdv1.get()) == 22:
                                if int(wdv2.get()) == 2:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00162').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 3:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00194').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 4:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00220').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 5:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00245').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 6:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00265').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                                if int(wdv2.get()) == 8:
                                    wd1.destroy()
                                    wd2 = Frame(root)
                                    wd2.grid(row=0, column=0, sticky=NSEW)
                                    Label(wd2, text='α = 0.00250').grid(row=0, column=0, sticky=W, pady=100, padx=10)
                                    Button(wd2, text="Start Over", command=maintab).place(x=30, y=450)
                                    wd2.tkraise()
                        Button(wd1, text='Next', command=next_wd2).place(x=405, y=450)
                        Button(wd1, text='Start Over', command=maintab).place(x=30, y=450)
                        wd1.tkraise()
                
                bwd1 = Button(wd, text='Next', command=next_wd).place(x=405, y=450)
                bwd2 = Button(wd, text='Start Over', command=maintab).place(x=30, y=450)
                wd.tkraise()
            wood()
        
        elif r.get() == 1:
            True
            #Metaltab()

    
    b1 = Button(Main, text='Next', command= nextstep_1).place(x=405, y=450) 


    Main.tkraise()


maintab()


root.mainloop()

