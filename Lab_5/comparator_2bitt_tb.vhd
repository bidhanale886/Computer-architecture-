    library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity comparator_2bitt_tb is
end comparator_2bitt_tb;

architecture Behavioral of comparator_2bitt_tb is
    component comparator_2bitt
        Port ( A       : in  STD_LOGIC_VECTOR (1 downto 0);
               B       : in  STD_LOGIC_VECTOR (1 downto 0);
               greater : out STD_LOGIC;
               equal   : out STD_LOGIC;
               less    : out STD_LOGIC);
    end component;
    signal A_tb : STD_LOGIC_VECTOR(1 downto 0) := "00";
    signal B_tb : STD_LOGIC_VECTOR(1 downto 0) := "00";
    signal greater_tb : STD_LOGIC;
    signal equal_tb   : STD_LOGIC;
    signal less_tb    : STD_LOGIC;

begin

    uut: comparator_2bitt PORT MAP (
          A => A_tb,
          B => B_tb,
          greater => greater_tb,
          equal => equal_tb,
          less => less_tb
        );

    stim_proc: process
    begin		
        for i in 0 to 3 loop
            for j in 0 to 3 loop
                A_tb <= std_logic_vector(to_unsigned(i, 2));
                B_tb <= std_logic_vector(to_unsigned(j, 2));
                wait for 10 ns;
            end loop;
        end loop;
        wait;
    end process;

end Behavioral;