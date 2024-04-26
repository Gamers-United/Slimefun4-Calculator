#  Copyright 2023 Macauley Lim xmachd@gmail.com
#  This code is licensed under GNU AFFERO GENERAL PUBLIC LICENSE v3.0.
#  A copy of this license should have been provided with the code download, if not see https://www.gnu.org/licenses/
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
#  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU AGPL v3.0 for more details.

class AcquisitionWrongType(Exception):
    def __init__(self):
        if self.args:
            self.message = self.args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Aquisitions are only used for base ingredients to add useful descriptions to how to get the item. Otherwise, for calculated entries use recipe adders. {self.message}"
        else:
            return f"Aquisitions are only used for base ingredients to add useful descriptions to how to get the item. Otherwise, for calculated entries use recipe adders."
