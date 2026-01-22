import ctypes
import ctypes.wintypes as wt

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101

# FIX: define LRESULT manually
LRESULT = ctypes.c_longlong if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_long

class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", wt.DWORD),
        ("scanCode", wt.DWORD),
        ("flags", wt.DWORD),
        ("time", wt.DWORD),
        ("dwExtraInfo", wt.ULONG_PTR)
    ]

LowLevelKeyboardProc = ctypes.WINFUNCTYPE(
    LRESULT,
    wt.INT,
    wt.WPARAM,
    wt.LPARAM
)

def hook_proc(nCode, wParam, lParam):
    if nCode == 0:
        kb = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        if wParam == WM_KEYDOWN:
            print(f"KEY DOWN: VK={kb.vkCode} SCAN={kb.scanCode}")
        elif wParam == WM_KEYUP:
            print(f"KEY UP: VK={kb.vkCode} SCAN={kb.scanCode}")
    return user32.CallNextHookEx(None, nCode, wParam, lParam)

hook = LowLevelKeyboardProc(hook_proc)

hHook = user32.SetWindowsHookExW(
    WH_KEYBOARD_LL,
    hook,
    kernel32.GetModuleHandleW(None),
    0
)

if not hHook:
    raise ctypes.WinError()

msg = wt.MSG()
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageW(ctypes.byref(msg))
