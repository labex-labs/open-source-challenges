# 介绍自动化测试

## 什么是自动化测试？

测试是用于检查代码运行情况的程序。

测试在不同层面进行。有些测试可能针对极小的细节（“某个特定的模型方法是否按预期返回值？”），而其他测试则检查软件的整体运行情况（“在网站上进行一系列用户输入是否能产生预期结果？”）。这与你在《设置数据库》中早期所做的测试并无不同，当时你使用 `shell` 来检查方法的行为，或者运行应用程序并输入数据以检查其表现。

自动化测试的不同之处在于，测试工作由系统为你完成。你只需创建一组测试，然后在对应用程序进行更改时，就可以检查代码是否仍按你最初的意图运行，而无需进行耗时的手动测试。

## 为何需要创建测试

那么，为什么要创建测试，又为什么现在创建呢？

你可能觉得仅仅学习 Python/Django 就已经忙得不可开交了，再去学习和做另一件事可能会让人应接不暇，甚至觉得没有必要。毕竟，我们的投票应用程序目前运行得相当顺利；费劲去创建自动化测试并不会让它运行得更好。如果创建投票应用程序是你做的最后一点 Django 编程工作，那么确实，你无需知道如何创建自动化测试。但是，如果并非如此，那么现在就是学习的绝佳时机。

### 测试能为你节省时间

在一定程度上，“检查它似乎能正常工作”将是一种令人满意的测试。在一个更复杂的应用程序中，组件之间可能会有数十种复杂的交互。

这些组件中的任何一个发生变化都可能对应用程序的行为产生意想不到的后果。检查它是否仍然“似乎能正常工作”可能意味着使用二十种不同的测试数据变体来遍历代码的功能，以确保你没有破坏任何东西——这可不是利用时间的好方法。

当自动化测试能在几秒钟内为你完成这项工作时，情况尤其如此。如果出了问题，测试还将有助于识别导致意外行为的代码。

有时，从富有成效的创造性编程工作中抽身去面对编写测试这种平淡无奇且无趣的事情，可能会让人觉得是件苦差事，尤其是当你知道你的代码运行正常的时候。

然而，编写测试的任务比花几个小时手动测试应用程序或试图找出新出现问题的原因要充实得多。

### 测试不仅能识别问题，还能预防问题

仅仅将测试视为开发的一个负面方面是错误的。

没有测试，应用程序的目的或预期行为可能相当模糊。即使是你自己的代码，有时你也会发现自己在其中四处摸索，试图弄清楚它到底在做什么。

测试改变了这一点；它们从内部照亮你的代码，当出现问题时，它们会将注意力集中在出错的部分——即使你甚至都没有意识到它出了问题。

### 测试会让你的代码更有吸引力

你可能创建了一个很棒的软件，但你会发现许多其他开发者会拒绝查看它，因为它没有测试；没有测试，他们就不会信任它。Django 的原始开发者之一雅各布·卡普兰 - 莫斯（Jacob Kaplan - Moss）说：“没有测试的代码从设计上就是有缺陷的。”

其他开发者在认真对待你的软件之前希望看到测试，这也是你开始编写测试的另一个原因。

### 测试有助于团队协作

前面几点是从单个开发者维护应用程序的角度写的。复杂的应用程序将由团队维护。测试可确保同事不会无意中破坏你的代码（并且你也不会在不知情的情况下破坏他们的代码）。如果你想以 Django 程序员为生，你必须擅长编写测试！
