Objective
============================================

In this example, there is only one objective to maximize, which is the total cost of goods sold:

.. math::
   total\_cost = total\_prod\_cost + total\_trans\_cost,

where each term in the RHS is defined as:

.. math::
   total\_prod\_cost & = \sum_{\substack{f \in \mathcal{F}\\ t\in \mathcal{T}}} prod\_cost_{f, t}, \\
   total\_trans\_cost & = \sum_{\substack{f \in \mathcal{F}\\ c \in \mathcal{C}\\ t\in \mathcal{T}}} trans\_cost_{f, c, t}.

