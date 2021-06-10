def cupy_check():
    try:
        import cupy as cp
        now_device = cp.cuda.runtime.getDeviceCount()
        if now_device == 0:
            return False, 0, "no device available"
        else:
            return True, 1, "now device : " + str(now_device)
    except:
        return False, -1,  "no cupy available"
