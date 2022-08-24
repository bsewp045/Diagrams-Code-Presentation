from diagrams import Diagram
from diagrams.k8s.compute import Pod

with Diagram("Simple Diagram", show=False):
    Pod("pod instance")