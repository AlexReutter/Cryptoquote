from Tkinter import *
from tkFileDialog import *
from cryptoquote import *
import sys, os, random


################### CLASS DEFINITIONS ######################
class CryptoApp(Frame):
    def __init__(self, parent=0):
        Frame.__init__(self,parent)
        self.master.title('Cryptoquoter')
        self.buildUI()

    def buildUI(self):
		# input file information: File name and type
		fFile = Frame(self)
		Label(fFile, text="File to be cryptoquoted: ").pack(side="left")
		self.eName = Entry(fFile)
		self.eName.insert(INSERT,"quote.txt")
		self.eName.pack(side="left", padx=5)
		# add frame for browse button
		fBrowse = Frame(fFile, borderwidth=1, relief=SUNKEN)
		self.bBrowse = Button(fBrowse, text="Browse", command=self.doBrowse)
		self.bBrowse.pack(side="top")
		fBrowse.pack(side="left", padx=3)
		fFile.pack(side="top", fill=X, pady=3)

		# output file information: File name and type
		fFile2 = Frame(self)
		Label(fFile2, text="Output file: ").pack(side="left")
		self.eName2 = Entry(fFile2)
		self.eName2.insert(INSERT,"cryptoquote.txt")
		self.eName2.pack(side="left", padx=5)
		# add frame for browse button
		fBrowse2 = Frame(fFile2, borderwidth=1, relief=SUNKEN)
		self.bBrowse2 = Button(fBrowse2, text="Browse", command=self.doSave)
		self.bBrowse2.pack(side="top")
		fBrowse2.pack(side="left", padx=3)
		fFile2.pack(side="top", fill=X, pady=3)

		# the text box holds the output, pad it to give a border
		self.txtBox = Text(self, width=60, height=10)
		self.txtBox.pack(side=TOP, padx=3, pady=3)

		# finally put some command buttons on to do the real work
		fButts = Frame(self)
		self.bCrypto = Button(fButts,
		                    text="Cryptoquote",
				    command=self.CryptoEvent)
		self.bCrypto.pack(side=LEFT, anchor=W, padx=50, pady=2)
		self.bReset = Button(fButts,
		                     text="Reset", command=self.doReset)
		self.bReset.pack(side=LEFT, padx=10)
		self.bQuit = Button(fButts,
		                    text="Quit",
				    command=self.doQuitEvent)
		self.bQuit.pack(side=RIGHT, anchor=E, padx=50, pady=2)

		fButts.pack(side=BOTTOM, fill=X)
	        self.pack()

    ################# EVENT HANDLING METHODS ####################
    # time to die...
    def doQuitEvent(self):
        import sys
        sys.exit()

    # create save event
    def doSave(self):
    	output_filename = asksaveasfilename()
    	self.eName2.delete('0',END)
    	self.eName2.insert(INSERT,output_filename)

	# create browse event
    def doBrowse(self):
        input_filename = askopenfilename()
        self.eName.delete('0',END)
        self.eName.insert(INSERT,input_filename)

    # restore default settings
    def doReset(self):
        self.txtBox.delete('1.0', END)

    # Create appropriate document type and analyze it.
    # then display the results in the form
    def CryptoEvent(self):
        input_filename = self.eName.get()
        output_filename = self.eName2.get()
	if input_filename == "":
		self.txtBox.insert(END,"\nNo input filename provided!\n")
		return
	if output_filename == "":
		self.txtBox.insert(END,"\nNo output filename provided!\n")
		return
	self.txtBox.insert(END, "\nCryptoquoting...\n")
       	cryptoquote(input_filename, output_filename)
	self.txtBox.insert(END, "\nDone\n")


#################  END OF CLASS DEFINITIONS ################
myApp = CryptoApp()
myApp.mainloop()

