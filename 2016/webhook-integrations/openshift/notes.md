# OpenShift

[OpenShift](https://www.openshift.com/) is a PaaS (Platform-as-a-Service), quite
similar to Heroku, that allows deploying and scaling cloud applications easily.

Some action hooks are provided on OpenShift environments, that basically are
scripts executed when the application passes one of these phases:

 - pre-build
 - build
 - deploy
 - post-deploy

Each phase has its own action hook, as it happens with Git hooks.

Action hooks are located in `App_Name/.openshift/action_hooks/<action>`, being
`<action>` one of the 4 phases listed above, as stated in OpenShift's
[docs](https://access.redhat.com/documentation/en-US/OpenShift_Online/2.0/html/User_Guide/Build_and_Deployment_Action_Hooks2.html).

A clear example on how can this be made is present in Zulip's
[Python bindings and examples](https://chat.zulip.org/api/), especially the one
in `zulip-x.x.x/integrations/git/post-receive`.
