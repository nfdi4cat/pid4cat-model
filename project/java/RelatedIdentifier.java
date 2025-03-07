package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  A base class for all types of related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedIdentifier  {

  private String type;

}
