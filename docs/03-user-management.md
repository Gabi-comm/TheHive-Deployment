# 3. Organization and user management

TheHive is multi-tenant: cases, observables, and tasks belong to an **organization**. The
built-in `admin` account administers the platform but does not work cases — analysts get their
own accounts inside a dedicated organization.

## 3.1 Create the SOC organization

Sign in as `admin@thehive.local`, open **Organizations**, and create one named `SOC`.

![Create the organization](images/13-create-organization.png)

Open it once created.

![The SOC organization](images/14-soc-organization.png)

## 3.2 Add an analyst

Inside the organization, open the **Users** tab and click **Add user**.

![Add user button](images/15-add-user-button.png)

Fill in the login, full name, and profile. Use `analyst` for a working SOC analyst — it grants
case and observable handling without organization administration. Reserve `org-admin` for
whoever manages the organization itself.

![Add user form](images/16-add-user-form.png)

## 3.3 Set the analyst password

New accounts have no password. Hover the user's row and click the **key / eye** icon in the
password column.

![Set password icon](images/17-set-user-password-icon.png)

Set a password for the account.

![Set the analyst password](images/18-set-analyst-password.png)

> Set a unique password per analyst and distribute it out of band. Placeholder passwords must
> never be committed to this repository.

## 3.4 Verify least privilege

Log out and sign back in with the analyst credentials.

![Analyst login](images/19-analyst-login.png)

The analyst lands in the `SOC` organization and can create and work cases, with no access to
platform administration — confirming the separation of duties.

![Analyst dashboard](images/20-analyst-dashboard.png)

Next: [operations](04-operations.md).
