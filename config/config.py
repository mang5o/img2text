def get_available_letters():
    now_available_letters = 'abcdefghijklmnopqrstuvwxyz\
                            ABCDEFGHIJKLMNOPQRSTUVWXYZ\
                            `1234567890-=\
                            ~!@#$%^&*()_+\
                            /<>{}[],.\|'
    return list(now_available_letters)
