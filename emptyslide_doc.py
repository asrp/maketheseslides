from node import Node
from numpy import array
from const import P, exr, exc
from persistent_doc.document import pmap
import node
node.node_num = 125031
root = Node("group", id='root', children = [
  Node("group", id='references', children = [
    Node("arc", id='point_icon', radius=5, fill_color=(0, 0, 0.5), p_center=P(0, 0))]),
  Node("group", skip_points=True, transforms={'dummy': None, 'zoom': ('scale', array([ 1.,  1.])), 'scroll_xy': ('translate', array([ 0.,  0.]))}, id='drawing', children = [
    Node("group", visible=True, id='custom_ui', children = [
      Node("text", id='n_14', value=exr('`selection.root'), p_botleft=P(34.0, 580.0)),
      Node("text", value=u'!doc.save()', id='n_18', on_click=u'doc.save()', font_size=13.777999999999997, p_botleft=P(195.0, 580.0)),
      Node("text", value=u'!doc.load()', id='n_20', on_click=u'doc.load()', font_size=13.777999999999997, p_botleft=P(197.0, 542.0)),
      Node("text", value=u'!paste_text()', id='n_1037', on_click=u'paste_text()', font_size=16.599999999999998, p_botleft=P(191.0, 631.0)),
      Node("text", value=u'!add_slide()', id='n_1120', on_click=u'add_slide()', font_size=11.5, p_botleft=P(383.0, 637.0)),
      Node("text", value=u"!add_slide(doc['editor.slide.id'])", id='n_1627', on_click=u"add_slide(doc['editor.slide.id'])", font_size=11.5, p_botleft=P(340.0, 581.0)),
      Node("text", value=u'!add_appear_transition()', id='n_2228', on_click=u'add_appear_transition()', font_size=11.5, p_botleft=P(340.0, 550.0)),
      Node("text", id='n_4026', value=u'!test_setstate()', on_click=u'test_setstate()', p_botleft=P(504.0, 624.0)),
      Node("text", value=u'!add_fadein_transitiofdsfsatdfsaidzzzzzzz', id='n_4191', on_click=u'add_fadein_transition()', font_size=11.5, p_botleft=P(338.0, 522.0)),
      Node("text", value=u'!center_title()', id='n_5154', on_click=u'center_title()', font_size=11.435739999999997, p_botleft=P(613.0, 520.0)),
      Node("text", value=u'!bullet_points_align()', id='n_27338', on_click=u'bullet_points_align()', font_size=11.435739999999997, p_botleft=P(615.0, 556.0)),
      Node("text", id='n_76413', value='![simplify_transform(node) for node in selected_nodes()]', font_size=11.5, p_botleft=P(192.0, 721.0)),
      Node("text", value=u'!distribute(selected_nodes(), axis=1, spacing=12)', id='n_38673', on_click=u'distribute(selected_nodes(), axis=1, spacing=12)', font_size=11.5, p_botleft=P(192.0, 785.0)),
      Node("text", value=u'!align(selected_nodes(), side=1, axis=1)', id='n_72359', on_click=u'align(selected_nodes(), side=1, axis=1)', font_size=11.435739999999997, p_botleft=P(191.0, 753.0)),
      Node("text", value=u'!paste_styled()', id='n_85155', on_click=u'paste_styled()', font_size=16.599999999999998, p_botleft=P(193.0, 668.0))]),
    Node("group", visible=exr('`editor.slide.id == `self.id'), t=0, id='slide1'),
    Node("group", t=0, id='slide2', count=0, visible=exr('`editor.slide.id == `self.id')),
    Node("group", t=0, id='slide3', count=0, visible=exr('`editor.slide.id == `self.id')),
  ]),
  Node("group", id='ui', children = [
    Node("group", slide=exr('`slide1'), grabbed=None, key_char=u'P', focus='n_38673', mouse_txy=P(236.0, 569.0), slides=['slide1', 'slide2', 'slide3'], grid=-2, drag_start=None, mode='edit', window_height=600, text_root='drawing', selected=pmap({}), gui_selected=None, id='editor', filename='emptyslide_doc.py', callbacks=pmap({}), stroke_color=(0, 0.5, 0), key_name='p', window_width=800, mouse_xy=P(236, 569), key_mods=['shift'], p_lastxy=P(0, 0), children = [
      Node("path", stroke_color=(0, 0.5, 0), child_id='path', id='n_3'),
      Node("text", id='n_4', value=None, child_id='text', botleft=exr('`self.parent.lastxy'))]),
    Node("group", id='overlay', transforms=exr('`drawing.transforms'), children = [
      Node("group", root='slide1', id='selection'),
      Node("group", skip_points=True, id='selection_bbox', stroke_color=(0.5, 0, 0), dash=([5, 5], 0), children = [
        Node("path", visible=exc('len(`selection) > 1'), corners=exc('(`selection).bbox()'), topright=exr('topright(`self.corners)'), id='n_10', botleft=exr('botleft(`self.corners)'), p_botright=exr('`self.parent.corners[1]'), p_topleft=exr('`self.parent.corners[0]'), children = [
          Node("line", start=exr('`self.parent.topleft'), end=exr('`self.parent.topright'), id='n_6'),
          Node("line", start=exr('`self.parent.topright'), end=exr('`self.parent.botright'), id='n_7'),
          Node("line", start=exr('`self.parent.botright'), end=exr('`self.parent.botleft'), id='n_8'),
          Node("line", start=exr('`self.parent.botleft'), end=exr('`self.parent.topleft'), id='n_9')])])])]),
  Node("group", id='animations'),
  Node("group", id='timer', paused=True, start=1527088248.983964, total=1029610.3888058662)])
