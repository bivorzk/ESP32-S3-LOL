import cv2
import numpy as np
import pyautogui as pg
import win32api, win32con, win32gui, win32com.client
import time
import path as p
import os


play = cv2.imread("images/Play_Button.png", cv2.IMREAD_UNCHANGED)
if play is None:
    raise FileNotFoundError("Play_Button.png doesn't exist.")
if play.shape[2] == 4:
    # RGBA to RGB
    play = cv2.cvtColor(play, cv2.COLOR_BGRA2BGR)
play_gray = cv2.cvtColor(play, cv2.COLOR_BGR2GRAY)

coopvsai = cv2.imread("images/CoopVsAI.png", cv2.IMREAD_UNCHANGED)
if coopvsai is None:
    raise FileNotFoundError("CoopVsAI.png doesn't exist.")
if coopvsai.shape[2] == 4:
    # RGBA to RGB
    coopvsai = cv2.cvtColor(coopvsai, cv2.COLOR_BGRA2BGR)
coopvsai_gray = cv2.cvtColor(coopvsai, cv2.COLOR_BGR2GRAY)

ChampSelect = cv2.imread("images/champ_select.png", cv2.IMREAD_UNCHANGED)
if ChampSelect is None:
    raise FileNotFoundError("Champ_Select.png doesn't exist.")
if ChampSelect.shape[2] == 4:
    # RGBA to RGB
    ChampSelect = cv2.cvtColor(ChampSelect, cv2.COLOR_BGRA2BGR)
ChampSelect_gray = cv2.cvtColor(ChampSelect, cv2.COLOR_BGR2GRAY)

selectMode = cv2.imread("images/confirm.png", cv2.IMREAD_UNCHANGED)
if selectMode is None:
    raise FileNotFoundError("Confirm.png doesn't exist.")
if selectMode.shape[2] == 4:
    # RGBA to RGB
    selectMode = cv2.cvtColor(selectMode, cv2.COLOR_BGRA2BGR)
selectMode_gray = cv2.cvtColor(selectMode, cv2.COLOR_BGR2GRAY)


findMatch = cv2.imread("images/find_match.png", cv2.IMREAD_UNCHANGED)
if findMatch is None:
    raise FileNotFoundError("FindMatch.png doesn't exist.")
if findMatch.shape[2] == 4:
    # RGBA to RGB
    findMatch = cv2.cvtColor(findMatch, cv2.COLOR_BGRA2BGR)
findMatch_gray = cv2.cvtColor(findMatch, cv2.COLOR_BGR2GRAY)


AcceptGame = cv2.imread("images/accept.png", cv2.IMREAD_UNCHANGED)
if AcceptGame is None:
    raise FileNotFoundError("Accept.png doesn't exist.")
if AcceptGame.shape[2] == 4:
    # RGBA to RGB
    AcceptGame = cv2.cvtColor(AcceptGame, cv2.COLOR_BGRA2BGR)
AcceptGame_gray = cv2.cvtColor(AcceptGame, cv2.COLOR_BGR2GRAY)


SearchBar = cv2.imread("images/search_bar.png", cv2.IMREAD_UNCHANGED)
if SearchBar is None:
    raise FileNotFoundError("Search_Bar.png doesn't exist.")
if SearchBar.shape[2] == 4:
    # RGBA to RGB
    SearchBar = cv2.cvtColor(SearchBar, cv2.COLOR_BGRA2BGR)
SearchBar_gray = cv2.cvtColor(SearchBar, cv2.COLOR_BGR2GRAY)


PickSion = cv2.imread("images/Sion.png", cv2.IMREAD_UNCHANGED)
if PickSion is None:
    raise FileNotFoundError("Sion.png doesn't exist.")
if PickSion.shape[2] == 4:
    # RGBA to RGB
    PickSion = cv2.cvtColor(PickSion, cv2.COLOR_BGRA2BGR)
PickSion_gray = cv2.cvtColor(PickSion, cv2.COLOR_BGR2GRAY)


lockin = cv2.imread("images/LOCK_IN.png", cv2.IMREAD_UNCHANGED)
if lockin is None:
    raise FileNotFoundError("LOCK_IN.png doesn't exist.")
if lockin.shape[2] == 4:
    # RGBA to RGB
    lockin = cv2.cvtColor(lockin, cv2.COLOR_BGRA2BGR)
lockin_gray = cv2.cvtColor(lockin, cv2.COLOR_BGR2GRAY)

while True:
    screen = pg.screenshot()
    screen_np = np.array(screen)
    if screen_np.shape[2] == 4:
        screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
    # Step 1: Click Play button
    result_play = cv2.matchTemplate(screen_gray, play_gray, cv2.TM_CCOEFF_NORMED)
    loc_play = np.where(result_play >= 0.7)
    if len(loc_play[0]) > 0:
        y, x = loc_play[0][0], loc_play[1][0]
        win32api.SetCursorPos((x + play.shape[1] // 2, y + play.shape[0] // 2))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(2)

        # Click CoopVsAI button
        while True:
            screen = pg.screenshot()
            screen_np = np.array(screen)
            if screen_np.shape[2] == 4:
                screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            screen_gray = screen_gray.astype(np.uint8)
            result_coop = cv2.matchTemplate(screen_gray, coopvsai_gray, cv2.TM_CCOEFF_NORMED)
            loc_coop = np.where(result_coop >= 0.7)
            if len(loc_coop[0]) > 0:
                y, x = loc_coop[0][0], loc_coop[1][0]
                win32api.SetCursorPos((x + coopvsai.shape[1] // 2, y + coopvsai.shape[0] // 2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(2)
                break
            time.sleep(2)
        # Apply selected mode
        while True:
            screen = pg.screenshot()
            screen_np = np.array(screen)
            if screen_np.shape[2] == 4:
                screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            screen_gray = screen_gray.astype(np.uint8)
            result_select = cv2.matchTemplate(screen_gray, selectMode_gray, cv2.TM_CCOEFF_NORMED)
            loc_select = np.where(result_select >= 0.6)
            if len(loc_select[0]) > 0:
                y, x = loc_select[0][0], loc_select[1][0]
                win32api.SetCursorPos((x + selectMode.shape[1] // 2, y + selectMode.shape[0] // 2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(2)
                break
            time.sleep(2)
        # Apply selected mode
        while True:
            screen = pg.screenshot()
            screen_np = np.array(screen)
            if screen_np.shape[2] == 4:
                screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
            screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
            screen_gray = screen_gray.astype(np.uint8)
            result_apply = cv2.matchTemplate(screen_gray, selectMode_gray, cv2.TM_CCOEFF_NORMED)
            loc_apply = np.where(result_apply >= 0.55)
            if len(loc_apply[0]) > 0:
                y, x = loc_apply[0][0], loc_apply[1][0]
                win32api.SetCursorPos((x + selectMode.shape[1] // 2, y + selectMode.shape[0] // 2))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            # print("//////////////////////////////////////////")
            time.sleep(2)
            break
        # Find Match button
     #   print("test")
    while True:
        print("----------------------------------------")
        screen = pg.screenshot() 
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_find = cv2.matchTemplate(screen_gray, findMatch_gray, cv2.TM_CCOEFF_NORMED)
        print(np.max(result_find))
        loc_find = np.where(result_find >= 0.65)
        if len(loc_find[0]) > 0:
            y, x = loc_find[0][0], loc_find[1][0]
            win32api.SetCursorPos((x + findMatch.shape[1] // 2, y + findMatch.shape[0] // 2))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            if (win32api.GetKeyState(0x1) & 0x8000):  # Pause if left mouse button has been clicked)
                break
            time.sleep(2)
        break
    # Accept Game button
    while True:
        screen = pg.screenshot()
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_accept = cv2.matchTemplate(screen_gray, AcceptGame_gray, cv2.TM_CCOEFF_NORMED)
        loc_accept = np.where(result_accept >= 0.65)
        if len(loc_accept[0]) > 0:
            y, x = loc_accept[0][0], loc_accept[1][0]
            win32api.SetCursorPos((x + AcceptGame.shape[1] // 2, y + AcceptGame.shape[0] // 2))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(2)
            break
        time.sleep(5)

    # Champ Select Implementation Here ---------------------
    while True:
        screen = pg.screenshot()
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_champ = cv2.matchTemplate(screen_gray, ChampSelect_gray, cv2.TM_CCOEFF_NORMED)
        loc_champ = np.where(result_champ >= 0.7)
        if len(loc_accept[0]) > 0:
            y, x = loc_accept[0][0], loc_accept[1][0]
            win32api.SetCursorPos((x + SearchBar.shape[1] // 2, y + SearchBar.shape[0] // 2))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(1)
            pg.typewrite("Sion", interval=0.1)
            time.sleep(2)
            break
    
    while True:
        screen = pg.screenshot()
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_pick = cv2.matchTemplate(screen_gray, PickSion_gray, cv2.TM_CCOEFF_NORMED)
        loc_pick = np.where(result_pick >= 0.7)
        if len(loc_pick[0]) > 0:
            y, x = loc_pick[0][0], loc_pick[1][0]
            win32api.SetCursorPos((x + PickSion.shape[1] // 2, y + PickSion.shape[0] // 2))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(2)
            break
    while True:
        screen = pg.screenshot()
        screen_np = np.array(screen)
        if screen_np.shape[2] == 4:
            screen_np = cv2.cvtColor(screen_np, cv2.COLOR_RGBA2RGB)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        screen_gray = screen_gray.astype(np.uint8)
        result_lockin = cv2.matchTemplate(screen_gray, lockin_gray, cv2.TM_CCOEFF_NORMED)
        loc_lockin = np.where(result_lockin >= 0.7)
        if len(loc_lockin[0]) > 0:
            y, x = loc_lockin[0][0], loc_lockin[1][0]
            win32api.SetCursorPos((x + lockin.shape[1] // 2, y + lockin.shape[0] // 2))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(2)
            break
    

    


 