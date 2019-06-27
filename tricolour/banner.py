# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


_BANNER = """
***********************************************************************************************************************************************
{0:s} ▄▄▄▄▄▄▄▄▄▄▄ {1:s} ▄▄▄▄▄▄▄▄▄▄▄{2:s}  ▄▄▄▄▄▄▄▄▄▄▄{3:s}  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄
{0:s}▐░░░░░░░░░░░▌{1:s}▐░░░░░░░░░░░▌{2:s}▐░░░░░░░░░░░▌{3:s}▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
{0:s} ▀▀▀▀█░█▀▀▀▀{1:s} ▐░█▀▀▀▀▀▀▀█░▌{2:s} ▀▀▀▀█░█▀▀▀▀{3:s} ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌
{0:s}     ▐░▌    {1:s} ▐░▌       ▐░▌{2:s}     ▐░▌    {3:s} ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
{0:s}     ▐░▌    {1:s} ▐░█▄▄▄▄▄▄▄█░▌{2:s}     ▐░▌    {3:s} ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
{0:s}     ▐░▌    {1:s} ▐░░░░░░░░░░░▌{2:s}     ▐░▌    {3:s} ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
{0:s}     ▐░▌    {1:s} ▐░█▀▀▀▀█░█▀▀ {2:s}     ▐░▌    {3:s} ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀
{0:s}     ▐░▌    {1:s} ▐░▌     ▐░▌  {2:s}     ▐░▌    {3:s} ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌
{0:s}     ▐░▌    {1:s} ▐░▌      ▐░▌ {2:s} ▄▄▄▄█░█▄▄▄▄{3:s} ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌
{0:s}     ▐░▌    {1:s} ▐░▌       ▐░▌{2:s}▐░░░░░░░░░░░▌{3:s}▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
{0:s}      ▀     {1:s}  ▀         ▀ {2:s} ▀▀▀▀▀▀▀▀▀▀▀ {3:s} ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀

Viva la révolution!

SARAO END USER LICENSE AGREEMENT

A DASK distributed RFI flagger by Science Data Processing and Radio Astronomy Research Group
Copyright 2019 South African Radio Astronomy Observatory (SARAO, SKA-SA). All rights reserved

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED GRATIS, "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. NO PORTION OF THIS SOFTWARE MAY BE REVERSE ENGINEERED OR INCLUDED IN OTHER 
PRODUCTS WITHOUT PRIOR WRITTEN PERMISSION FROM SARAO. THIS SOFTWARE, EITHER IN PORTION OR IN ITS ENTIRETY, MAY NOT BE SOLD OR OTHERWISE 
COMMERCIALLY EXPLOITED BY ANY THIRD PARTY

By using this software you, the end user, agree to these terms and conditions
***********************************************************************************************************************************************
"""  # noqa


def banner():
    RED = '\033[0;31m'
    WHITE = '\033[0;37m'
    BLUE = '\033[0;34m'
    RESET = '\033[0m'

    # make it Frenchy
    return _BANNER.format(BLUE, WHITE, RED, RESET)