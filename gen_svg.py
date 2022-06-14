import pydot
import subprocess
from pathlib import Path

cwd = Path(".")
for dot_file in cwd.rglob("*.dot"):
    # load dot file
    g = pydot.graph_from_dot_file(dot_file)

    # convert to svg file and open for preview
    svg_file = str(dot_file.with_suffix('.svg'))
    g[0].write_svg(svg_file)
    subprocess.call(("open", svg_file))