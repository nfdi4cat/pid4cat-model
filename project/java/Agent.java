package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  Data class for a person who plays a role relative to PID creation or curation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Agent  {

  private String name;
  private String emailAddress;
  private String orcid;
  private String affiliationRor;
  private String role;

}
