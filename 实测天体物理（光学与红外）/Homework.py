import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter

m_star = np.linspace(16, 28, num=1200, endpoint=True)
m_sky = [19, 21, 23]
D = [1, 4, 10]
d = [3, 1, 0.5, 0.1]
m_sky = [19, 21, 23]
t_list = []

# Question 1(1)

fig, ax = plt.subplots(figsize=(16, 10), dpi=250)

for Di in D:
    for m_stari in m_star:
        di = 1
        m_skyi = 21
        C1 = 4560298170.05966 * (10 ** (-0.4 * m_stari)) * (Di ** 2)
        C2 = 7163299614.619203 * \
            (10 ** (-0.4 * m_skyi)) * (Di ** 2) * (di ** 2)
        t = 100 * (C1 + C2) / (C1 ** 2)
        t_list.append(t)  # in minutes
    print('D(m) = ' + str(Di) + ', t(min) = ' + str([t_list[0], t_list[-1]]))
    ax.plot(m_star, t_list, label=r'$D = $' + str(Di) + r'$\,\mathrm{m}$')
    t_list = []

ax.set(xlabel=r'$m_{\mathrm{star}}\ (\mathrm{mag})$',
       ylabel=r'$t\ (\mathrm{s})$')
ax.grid(True, linestyle='-.')

ax.set_xticks(np.arange(16, 29, 1))

ax.set_yscale('log')
ax.set_ylim(0.0001,10000000)
locmaj = LogLocator(base=10,numticks=12) 
ax.yaxis.set_major_locator(locmaj)
locmin = LogLocator(base=10.0,subs=(1,2,3,4,5,6,7,8,9),numticks=12)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(NullFormatter())

ax.legend(loc='upper left')
plt.show()

# Question 1(2)

fig, ax = plt.subplots(figsize=(16, 10), dpi=250)

for di in d:
    for m_stari in m_star:
        Di = 4
        m_skyi = 21
        C1 = 4560298170.05966 * (10 ** (-0.4 * m_stari)) * (Di ** 2)
        C2 = 7163299614.619203 * \
            (10 ** (-0.4 * m_skyi)) * (Di ** 2) * (di ** 2)
        t = 100 * (C1 + C2) / (C1 ** 2)
        t_list.append(t)  # in minutes
    print('seeing disc(arcsec) = ' + str(di) +
          ', t(min) = ' + str([t_list[0], t_list[-1]]))
    ax.plot(m_star, t_list, label=r'$Seeing\ disc = $' +
             str(di) + r'$\,\mathrm{arcsec}$')
    t_list = []

ax.set(xlabel=r'$m_{\mathrm{star}}\ (\mathrm{mag})$',
       ylabel=r'$t\ (\mathrm{s})$')
ax.grid(True, linestyle='-.')

ax.set_xticks(np.arange(16, 29, 1))

ax.set_yscale('log')
ax.set_ylim(0.001,10000000)
locmaj = LogLocator(base=10,numticks=11) 
ax.yaxis.set_major_locator(locmaj)
locmin = LogLocator(base=10.0,subs=(1,2,3,4,5,6,7,8,9),numticks=12)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(NullFormatter())

ax.legend(loc='upper left')
plt.show()

# Question 1(3)

fig, ax = plt.subplots(figsize=(16, 10), dpi=250)

for m_skyi in m_sky:
    for m_stari in m_star:
        Di = 4
        di = 1
        C1 = 4560298170.05966 * (10 ** (-0.4 * m_stari)) * (Di ** 2)
        C2 = 7163299614.619203 * \
            (10 ** (-0.4 * m_skyi)) * (Di ** 2) * (di ** 2)
        t = 100 * (C1 + C2) / (C1 ** 2)
        t_list.append(t)  # in minutes
    print('m_sky(mag/arcsec^2) = ' + str(m_skyi) +
          ', t(min) = ' + str([t_list[0], t_list[-1]]))
    ax.plot(m_star, t_list, label=r'$Sky\ background\ brightness = $' +
             str(m_skyi) + r'$\,\mathrm{mag}$')
    t_list = []

ax.set(xlabel=r'$m_{\mathrm{star}}\ (\mathrm{mag})$',
       ylabel=r'$t\ (\mathrm{s})$')
ax.grid(True, linestyle='-.')

ax.set_xticks(np.arange(16, 29, 1))

ax.set_yscale('log')
ax.set_ylim(0.001,10000000)
locmaj = LogLocator(base=10,numticks=11) 
ax.yaxis.set_major_locator(locmaj)
locmin = LogLocator(base=10.0,subs=(1,2,3,4,5,6,7,8,9),numticks=12)
ax.yaxis.set_minor_locator(locmin)
ax.yaxis.set_minor_formatter(NullFormatter())

ax.legend(loc='upper left')
plt.show()


# Question 2

for Di in D:
    for di in d:
        m_star_list = []
        for m_skyi in m_sky:
            if Di == 1 and di == 0.1:
                di = 0.11862454
            C2 = 7163299614.619203 * \
                (10 ** (-0.4 * m_skyi)) * (Di ** 2) * (di ** 2)
            C1 = (1 + (1 + 144 * C2) ** 0.5) / 72
            m_star = -2.5 * np.log10(C1 / (4560298170.05966 * (Di ** 2)))
            m_star_list.append('%.3f' % m_star)
        print('D = ' + str(Di) + 'm, Seeing disc = ' + str(di) +
              'arcsec, m_star = ' + str(m_star_list) + 'mag')
