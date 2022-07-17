import importlib

renderer_list = ["reportlabPDF","pandocPDF","pandocHTML"]

renderer_dict = {}
renderer_req = {}

renderer_req = {}
renderer_req["reportlabPDF"] = ["reportlab",]
renderer_req["pandocPDF"] = ["pandoc",]
renderer_req["pandocHTML"] = ["pandoc",]

if importlib.util.find_spec("reportlab") is not None:
    from nest.renderer.reportlab_renderer import reportlabRenderer
    renderer_dict["reportlabPDF"] = reportlabRenderer

if importlib.util.find_spec("pandoc") is not None:
    from nest.renderer.pandoc_renderer import pandocHTML
    from nest.renderer.pandoc_renderer import pandocPdf
    renderer_dict["pandocHTML"] = pandocHTML
    renderer_dict["pandocPDF"] = pandocPdf
