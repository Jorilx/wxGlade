#!/usr/bin/env lisp
;;;
;;; generated by wxGlade
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxCL)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFrame)
(use-package :wxSizer)
(use-package :wxStaticText)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; end wxGlade


(defclass Bug184_Frame()
        ((top-window :initform nil :accessor slot-top-window)
        (label-1 :initform nil :accessor slot-label-1)
        (sizer-1 :initform nil :accessor slot-sizer-1)))

(defun make-Bug184_Frame ()
        (let ((obj (make-instance 'Bug184_Frame)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj Bug184_Frame))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: Bug184_Frame.__init__
        (setf (slot-label-1 obj) (wxStaticText_Create (slot-top-window obj) wxID_ANY (_"Just a label") -1 -1 -1 -1 0))
        ;;; end wxGlade
        )

(defmethod set-properties ((obj Bug184_Frame))
        ;;; begin wxGlade: Bug184_Frame.__set_properties
        (wxFrame_SetTitle (slot-top-window obj) (_"frame_1"))
        (wxWindow_SetBackgroundColour (slot-top-window obj) (wxSystemSettings_GetColour wxSYS_COLOUR_BACKGROUND))
        ;;; end wxGlade
        )

(defmethod do-layout ((obj Bug184_Frame))
        ;;; begin wxGlade: Bug184_Frame.__do_layout
        (setf (slot-sizer-1 obj) (wxBoxSizer_Create wxVERTICAL))
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-label-1 obj) 1 (logior wxALL wxEXPAND) 5 nil)
        (wxWindow_SetSizer (slot-top-window obj) (slot-sizer-1 obj))
        (wxSizer_Fit (slot-sizer-1 obj) (slot-top-window obj))
        (wxFrame_layout (slot-Frame184 self))
        ;;; end wxGlade
        )

;;; end of class Bug184_Frame


(defun init-func (fun data evt)
        (let ((Frame184 (make-Bug184_Frame)))
        (ELJApp_SetTopWindow (slot-top-window Frame184))
        (wxWindow_Show (slot-top-window Frame184))))
;;; end of class MyApp

    (setf (textdomain) "app") ;; replace with the appropriate catalog name
    (defun _ (msgid) (gettext msgid "app"))


(unwind-protect
    (Eljapp_initializeC (wxclosure_Create #'init-func nil) 0 nil)
    (ffi:close-foreign-library "../miscellaneous/wxc-msw2.6.2.dll"))
