Variables
============================================

Independent variables
--------------------------------

.. list-table:: :math:`f \in \mathcal{F}, ~c \in \mathcal{C}, ~t \in \mathcal{T}`
   :widths: 20 80
   :header-rows: 1

   * - Name
     - Description
   * - trans
     - Product amount [t] transported from factory :math:`f` to customer :math:`c` at time :math:`t`.


Dependent variables
--------------------------------

.. list-table:: :math:`f \in \mathcal{F}, ~t \in \mathcal{T}`
   :widths: 100
   :header-rows: 1

   * - Definition
   * - .. math:: prod_{f, t} = \sum_{c \in \mathcal{C}} trans_{f, c, t}
   * - .. math:: prod\_cost_{f, t} = \mathrm{prod\_uc}_f \times prod_{f, t}


.. list-table:: :math:`c \in \mathcal{C}, ~t \in \mathcal{T}`
   :widths: 100
   :header-rows: 1

   * - Definition
   * - .. math:: sell_{c, t} = \sum_{f \in \mathcal{F}} trans_{f, c, t}


.. list-table:: :math:`f \in \mathcal{F}, ~c \in \mathcal{C}, ~t \in \mathcal{T}`
   :widths: 100
   :header-rows: 1

   * - Definition
   * - .. math:: trans\_cost_{f, c, t} = \mathrm{trans\_uc}_{f, c} \times trans_{f, c, t}




