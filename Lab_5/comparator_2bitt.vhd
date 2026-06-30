library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity comparator_2bitt is
    Port ( A   : in  STD_LOGIC_VECTOR (1 downto 0);
           B   : in  STD_LOGIC_VECTOR (1 downto 0);
           greater : out STD_LOGIC;
           equal   : out STD_LOGIC;
           less    : out STD_LOGIC);
end comparator_2bitt;
architecture Dataflow of comparator_2bitt is
begin
    greater <= '1' when (A > B) else '0';
    equal   <= '1' when (A = B) else '0';
    less    <= '1' when (A < B) else '0';
end Dataflow;