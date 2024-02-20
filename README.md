# CV and midi sonfication and sequencing libary
 

A tool for the sequencing and modification of control voltage and midi signals via USB and the MCP4578 DAC. 


The intention of this project was that a user could leverage this artifact to programmatically control the modulation and playing of synthesizers live. Allowing them to concede aspects of their performance to external factors, may that be live web scraped data, or user input from an audience, or physical interactions in an art installment. This would provide a reactive, live element to the construction and composition of music.

Final System Architecture Overview
![image](https://github.com/De3pBlu3/CV-and-midi-sonification/assets/24615375/217147dc-928c-486d-8961-cf83539281ff)

As both MIDI and control voltage is required in tandem to alter a synthesizer's playing, the original design required that from a singular system center, both midi commands and serial communication to the arduino could be sent and altered. In order to accomplish this, a raspberry pi was selected to be a controller to the MIDI out and to alter control voltage.



However the Raspberry Pi utilizes a digital voltage range of 0V to 3.3V for its GPIO pins, and as such a digital to analog converter was required to output a consistent analog voltage between 0V and 5V, avoiding the use of pulse width modulation. Leveraging the Adafruit MCP4568 and its arduino based library, I was able to generate control voltages which could be altered via serial communication from the raspberry pi.



However both serial and MIDI communication is limited by their lack of polyphonic capabilities. While a single command sent to a serial input bus can contain multiple instructions, this increases computational overhead, which is of great concern on devices with low processing power in applications involving strict timing conditions such as music. As such a buffer of instruction was implemented for both MIDI and serial communication, allowing for the controller (the Raspberry Pi) to queue MIDI and serial instructions to be completed sequentially as they arrive in the queue and concurrent to the other components in another thread

Elements of the UNIX design philosophy were adhered to during development, in that both the MIDI and CV modules are self contained and can operate on their own accord or be utilized by other software. I viewed this modularity as an important facet of the design as other utilizations of the project could ensure a zero redundancy usage.

Melody generation is based upon the random selection of notes and timings from a generated scale when given a root and a chosen form of scale via intervals. 




DAC module circuit diagram
![image](https://github.com/De3pBlu3/CV-and-midi-sonification/assets/24615375/670ca657-1f65-4aa7-93c9-f0c5db2432d0)

Impact:
My purpose in creating a project which provided the tools to sonify data live was Inspired by works such as Hansen and Rubin’s Listening Post and the recent developments in post-internet art. Particularly I wished to create a tangible artifact which forms from the abstract of the internet and its habitants. Particularly I wish to sonify the ‘voices’ of the individual on the internet. In order to begin tackling an installment akin to that, I needed to create a library which would allow for a user to programmatically interface with instruments both virtual and physical in terms of their playing and modulation.


Applied use cases for the sequencer: 

During development, various applications of the sequencer were prototyped and tested for evaluation. These included a virtual gallery space (as depicted) which would react to the data which would be sonified in a visual form while playing the audio. Though this prototype was never completed, feedback from play tests returned positive. Primarily noting a desire for additional user interactivity.  Another application was a Discord bot (a script built upon the Discord application which is interactable via its chat functionality). This ‘bot’ allowed for users to interact with playing of the synths in real time. 
