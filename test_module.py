import medical_data_visualizer as mdv

def test_cat_plot():
    fig = mdv.draw_cat_plot()
    assert fig is not None


def test_heat_map():
    fig = mdv.draw_heat_map()
    assert fig is not None
