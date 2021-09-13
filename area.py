def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError('base and height must be 0+')
    return base * height * 0.5