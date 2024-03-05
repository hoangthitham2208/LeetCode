class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            new_row = []
            new_row.append(1)
            for i in range(1, len(row)):
                new_element = row[i - 1] + row[i]
                new_row.append(new_element)

            new_row.append(1)
            row = new_row
        return row
