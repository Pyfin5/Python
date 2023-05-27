""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		  		 			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			 	 	 		 		 	
or edited.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Student Name: Abdullah Shafi (replace with your name)  		  	   		  		 			  		 			 	 	 		 		 	
GT User ID: ashafi7 (replace with your User ID)  		  	   		  		 			  		 			 	 	 		 		 	
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import numpy as np  		  	   		
import matplotlib.pyplot as plt   		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def author():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: str  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return "ashafi7"  # replace tb34 with your Georgia Tech username.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def gtid():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: int  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return 900897987  # replace with your GT ID number  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	

  		  	   		  		 			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		  		 			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		  		 			  		 			 	 	 		 		 	
    """	  		     			  		 			 	 	 		 		 	
    result = False  		  	   		  		 			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			 	 	 		 		 	
        result = True  		  	   		  		 			  		 			 	 	 		 		 	
    return result 

def test_code():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Method to test your code  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    win_prob = 0.47  # set appropriately to the probability of a win  		  	   		  		 			  		 			 	 	 		 		 	
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			 	 	 		 		 	
    print(get_spin_result(win_prob))  # test the roulette spin  
    episode_simulation(get_spin_result, False)
    figure_1(episode_simulation,1000)
    figure_2_4(episode_simulation,10,1000)
    figure_3_5(episode_simulation,10,1000)
    


def episode_simulation(get_spin_result,bankroll):   
     episode_winnings = 0
     winnings_array = []
     i=0
     bankroll_indicator = bankroll
     while episode_winnings < 80 and i < 1000:
         won = Falsev
         bet_amount = 1
         while not won:
                 won = get_spin_result(win_prob)
                 if won == True:
                     episode_winnings = episode_winnings + bet_amount 
                     winnings_array.append(episode_winnings)
                     i = i+1
                 if won == False:
                     episode_winnings = episode_winnings - bet_amount
                     winnings_array.append(episode_winnings)
                     bet_amount = bet_amount * 2
                     i = i+1
                     if (episode_winnings - bet_amount < -256) and bankroll_indicator == True:
                           bet_amount = episode_winnings + 256
                     else: 
                           bet_amount = bet_amount * 2
                 while (episode_winnings <= -256 and i <1000 and bankroll_indicator == True):
                       episode_winnings = -256
                       winnings_array.append(episode_winnings)
                       i = i+1
                 while (episode_winnings >= 80 and i <1000):
                      episode_winnings >= 80
                      episode_winnings = 80
                      winnings_array.append(episode_winnings)
                      i = i+1
     return(winnings_array)


def figure_1(episode_simulation,i):
    fig, (ax1) = plt.subplots(nrows = 1,
                                  ncols = 1,
                                  figsize=(4,4)) 
    ax1.set_title('Figure 1')
    ax1.set_xlabel('No. of Trials')
    ax1.set_ylabel('Episode Winnings')
    ax1.set(xlim=(0, 300), ylim=(-256, 100))    
    for a in range(i):
        ax1.plot(episode_simulation(get_spin_result,False))
    

def figure_2_4(episode_simulation,i,j):
    fig, (ax1,ax2) = plt.subplots(nrows = 2,
                                  ncols = 1,
                                  figsize=(4,4)) 
    mean_episodes_i = []
    std_dev_episodes_i = []
    mean_episodes_j = []
    std_dev_episodes_j = []
    
    for a in range(i): 
        mean_episodes_i.append(np.mean(episode_simulation(get_spin_result,False)))
        std_dev_episodes_i.append(np.mean(episode_simulation(get_spin_result,False)))
    
    for a in range(j): 
        mean_episodes_j.append(np.mean(episode_simulation(get_spin_result,True)))
        std_dev_episodes_j.append(np.mean(episode_simulation(get_spin_result,True)))
    
    plt.subplots_adjust(hspace=2,wspace=0.5)
    ax1.set_title('Figure 1')
    ax1.set_xlabel('No. of Trials')
    ax1.set_ylabel('Episode Winnings')
    ax1.set(xlim=(0, 300), ylim=(0, 100))    
    ax2.set_title('Figure 2')
    ax2.set_xlabel('No. of Trials')
    ax1.set_ylabel('Episode Winnings')
    ax2.set(xlim=(0, 300), ylim=(0, 100))
    for a in range(i):
        ax1.plot(mean_episodes_i)
    for a in range(j):
        ax2.plot(mean_episodes_j)
        

def figure_3_5(episode_simulation,i,j):
    fig, (ax1,ax2) = plt.subplots(nrows = 2,
                                  ncols = 1,
                                  figsize=(4,4)) 
    median_episodes_i = []
    std_dev_episodes_i = []
    median_episodes_j = []
    std_dev_episodes_j = []
    
    for a in range(i): 
        median_episodes_i.append(np.mean(episode_simulation(get_spin_result,False)))
        std_dev_episodes_i.append(np.mean(episode_simulation(get_spin_result,False)))
    
    for a in range(j): 
        median_episodes_j.append(np.mean(episode_simulation(get_spin_result,True)))
        std_dev_episodes_j.append(np.mean(episode_simulation(get_spin_result,True)))
    
    plt.subplots_adjust(hspace=2,wspace=0.5)
    ax1.set_title('Figure 1')
    ax1.set_xlabel('No. of Trials')
    ax1.set_ylabel('Episode Winnings')
    ax1.set(xlim=(0, 300), ylim=(0, 100))    
    ax2.set_title('Figure 2')
    ax2.set_xlabel('No. of Trials')
    ax1.set_ylabel('Episode Winnings')
    ax2.set(xlim=(0, 300), ylim=(0, 100))
    for a in range(i):
        ax1.plot(median_episodes_i)
    for a in range(j):
        ax2.plot(median_episodes_j)
        

 			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    test_code()  		  	   		  		 			  		 			

