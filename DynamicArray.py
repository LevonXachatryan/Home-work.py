from typing import Any, Iterator, List, Optional, Union
import array
class DynamicArray:
    def __init__(self, capacity = 1, value = 0):
        self.capacity: int = capacity
        self.size: int = 0
        self.arr = array.array("i", self.capacity * [value])
        
    def __len__(self) -> int:
        return self.size
    
    @property
    def capacity(self) -> int:
        return self.capacity
    
    def __getitem__(self, index: int) -> Any:
        if index < 0 or index > self.size:
            raise IndexError("IndexError")
        return self.array[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        if index < 0 or index > self.size:
            raise IndexError("IndexError")
        return self.array[index]
    
    def _resize(self, newCapcity: int):
        new_arr: array[Union[int, None]] = [None] * newCapcity
        for i in range(self.size):
            self.arr[i] = new_arr[i]
        self.arr = new_arr
        self.capacity = newCapcity
        
    
    def append(self, value: int) -> int:
        if self.size >= self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1
            
    def __str__(self) -> str:
        return f"{[x for x in self.arr]}"
    

    def __repr__(self) -> str:
        return f"DynamicArray({self.__str__})"

        
    def __add__(self, other: "DynamicArray") -> "DynamicArray":
        if not isinstance(other, DynamicArray):
            raise TypeError("Error")
        res = DynamicArray(self.size + other.size)
        for i in range(self.size):
            res.append(self.array[i])
        for i in range(self.size):
            res.append(other[i])
        return res
    
    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            raise TypeError("Error")
        for i in range(other.size):
            self.append(other[i])
        return self
    
    def __eq__(self, other: "DynamicArray") -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.array[i] != other[i]:
                return False
        return True
        
    def __ne__(self, other: "DynamicArray") -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other: "DynamicArray") -> bool:
        return self.size < other.size
    
    def __le__(self, other: "DynamicArray") -> bool:
        return self.size <= other.size
    
    def __gt__(self, other: 'DynamicArray') -> bool:
        return self._size > other._size
    
    def __ge__(self, other: 'DynamicArray') -> bool:
        return self._size >= other._size
    
    def __iter__(self) -> Iterator[Any]:
        for i in range(self.size):
            return self.array[i]
        
    def __hash__(self) -> int:
        raise TypeError("type error")

if __name__ == "main":
    st1 = DynamicArray()
    st1.append(1)
    st1.append(2)    