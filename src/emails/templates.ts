// OFF by default as per constraints. No real outbound emails.
export const emailTemplates = {
  registrationReceived: (name: string) => `
    <h1>Registration Received</h1>
    <p>Hi ${name},</p>
    <p>We have received your registration for Lornette's Foundation Golf Program.</p>
    <p>We will be in touch shortly.</p>
  `,
  accountActivation: (name: string, link: string) => `
    <h1>Activate Your Account</h1>
    <p>Hi ${name},</p>
    <p>Please click the link below to activate your account:</p>
    <a href="${link}">${link}</a>
  `,
  clubInvite: (clubName: string, code: string) => `
    <h1>You've Been Invited</h1>
    <p>You have been invited to join the ${clubName} cohort.</p>
    <p>Use this invite code when registering: <strong>${code}</strong></p>
  `,
  cohortEnrollmentConfirmation: (name: string, cohortName: string) => `
    <h1>Enrollment Confirmed</h1>
    <p>Hi ${name},</p>
    <p>You have successfully been enrolled in ${cohortName}.</p>
  `
};
